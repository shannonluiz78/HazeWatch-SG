"""Download and validate NASA's public Suomi-NPP VIIRS export; no API key needed."""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import math
from pathlib import Path
import time
import urllib.request

SOURCE = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/SUOMI_VIIRS_C2_SouthEast_Asia_24h.csv'
ROOT = Path(__file__).resolve().parent.parent
UTC = dt.timezone.utc

def timestamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(UTC)

def inside(x, y, ring):
    result = False
    for a, b in zip(ring, ring[1:]):
        if (a[1] > y) != (b[1] > y) and x < (b[0]-a[0]) * (y-a[1]) / (b[1]-a[1]) + a[0]:
            result = not result
    return result

def build_payload(text, boundaries, now, previous=None):
    reader = csv.DictReader(io.StringIO(text.lstrip('\ufeff')))
    required = {'latitude','longitude','acq_date','acq_time','satellite','confidence','frp'}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError('NASA CSV schema changed or source returned an error page')
    points = {}
    rows = 0
    for row in reader:
        rows += 1
        if row['confidence'] not in ('nominal','high','low'):
            raise ValueError('Unexpected NASA confidence value')
        x, y, frp = float(row['longitude']), float(row['latitude']), float(row['frp'])
        if not all(math.isfinite(v) for v in (x,y,frp)) or not (-180 <= x <= 180 and -90 <= y <= 90 and frp >= 0):
            raise ValueError('Invalid NASA coordinate or FRP')
        acquisition = row['acq_time'].zfill(4)
        observed = timestamp(f"{row['acq_date']}T{acquisition[:2]}:{acquisition[2:]}:00Z")
        if observed > now + dt.timedelta(minutes=5):
            raise ValueError('NASA export contains future observations')
        if row['confidence'] == 'low' or not now-dt.timedelta(hours=24) <= observed <= now:
            continue
        if row['satellite'] not in ('N','Suomi-NPP','Suomi NPP'):
            raise ValueError('Unexpected satellite in Suomi-NPP export')
        for region, polygon in boundaries.items():
            if inside(x,y,polygon[0]) and not any(inside(x,y,hole) for hole in polygon[1:]):
                observed_iso = observed.isoformat().replace('+00:00','Z')
                identity = f"N|{x:.5f}|{y:.5f}|{observed_iso}"
                key = hashlib.sha256(identity.encode()).hexdigest()[:24]
                points[key] = dict(id=key,lon=x,lat=y,region=region,confidence=row['confidence'],frp=frp,timestamp=observed_iso)
                break
    # Reject an empty/misdated export, rather than silently publish a false regional zero.
    # A valid nonempty Southeast Asia export can legitimately have zero detections in our two regions.
    if not rows:
        raise ValueError('Empty NASA export; retain previous successful retrieval')
    # All rows may be out of date, including low-confidence or outside-region rows.
    all_times = [timestamp(f"{r['acq_date']}T{r['acq_time'].zfill(4)[:2]}:{r['acq_time'].zfill(4)[2:]}:00Z") for r in csv.DictReader(io.StringIO(text.lstrip('\ufeff')))]
    if max(all_times) < now-dt.timedelta(hours=24):
        raise ValueError('NASA source export is older than 24 hours')
    prior = None
    if previous and previous.get('schemaVersion') == 1 and previous.get('sourceUrl') == SOURCE:
        prior_time = timestamp(previous['retrievedAt'])
        if prior_time <= now:
            prior = previous
    old_ids = {p['id'] for p in prior['points']} if prior else set()
    values = sorted(points.values(), key=lambda p: (p['timestamp'],p['id']), reverse=True)
    new_ids = [p['id'] for p in values if p['id'] not in old_ids] if prior else []
    iso = lambda value: value.isoformat().replace('+00:00','Z')
    return dict(schemaVersion=1,sourceUrl=SOURCE,product='Suomi-NPP VIIRS 375 m Collection 2 NRT',
        retrievedAt=iso(now),windowStart=iso(now-dt.timedelta(hours=24)),windowEnd=iso(now),
        observationStart=min((p['timestamp'] for p in values),default=None),
        observationEnd=max((p['timestamp'] for p in values),default=None),
        comparedWith=prior['retrievedAt'] if prior else None,newIds=new_ids,points=values)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(ROOT/'data/hotspots.json'))
    parser.add_argument('--previous')
    parser.add_argument('--csv', help='Use a local export for validation instead of downloading')
    parser.add_argument('--now', help='Explicit UTC time for repeatable offline tests')
    args = parser.parse_args()
    boundaries = json.loads((ROOT/'scripts/hotspot-boundaries.json').read_text())['regions']
    previous = None
    if args.previous and Path(args.previous).exists():
        previous = json.loads(Path(args.previous).read_text())
    if args.csv:
        text = Path(args.csv).read_text(encoding='utf-8')
    else:
        for attempt in range(3):
            try:
                request = urllib.request.Request(SOURCE,headers={'User-Agent':'HazeWatchSG/1.0 (public FIRMS export)'})
                with urllib.request.urlopen(request,timeout=60) as response:
                    raw = response.read(30_000_001)
                    if len(raw) > 30_000_000: raise ValueError('NASA export exceeds safety limit')
                    text = raw.decode('utf-8')
                break
            except Exception:
                if attempt == 2: raise
                time.sleep(5 * (attempt+1))
    now = timestamp(args.now) if args.now else dt.datetime.now(UTC)
    payload = build_payload(text,boundaries,now,previous)
    output = Path(args.output)
    output.parent.mkdir(parents=True,exist_ok=True)
    temporary = output.with_suffix('.tmp')
    temporary.write_text(json.dumps(payload,separators=(',',':'))+'\n',encoding='utf-8')
    temporary.replace(output)
    print(f"Retrieved {payload['retrievedAt']}: {len(payload['points'])} detections; {len(payload['newIds'])} newly listed")

if __name__ == '__main__':
    main()
