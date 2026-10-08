# HazeWatchSG hourly NASA hotspot updates

Prepared for https://github.com/shannonluiz78/HazeWatch-SG (public repository; default branch: main).

Version 7 also fixes the gauge readout overlap and restores readings directly on the Singapore map on phones. The label above the map identifies the active metric and units; changing the metric switches all five map readings. The larger list below remains available for readability.

Checked on 8 October 2026: the live site still served the older frozen-snapshot HTML, the main branch contained only DESIGN.md, index.html and screen.png, and the hourly data address returned 404. The hourly workflow must be uploaded with this update before automatic retrieval can begin.

## Upload and activate

1. Extract the ZIP. Upload its contents to the **main** branch, keeping the folders and file names intact. Replace the existing `index.html` with the supplied one.
2. Required files are `index.html`, `vercel.json`, `.github/workflows/update-hotspots.yml`, `scripts/update_hotspots.py`, and `scripts/hotspot-boundaries.json`. The leading dot in `.github` matters. Uploading just the HTML cannot activate hourly updates.
3. If your upload tool hides `.github`, create the workflow directly on GitHub: Add file → Create new file → enter `.github/workflows/update-hotspots.yml`, copy the supplied workflow text, then commit to main. The scripts belong inside `scripts/`.
4. Open the repository's **Actions** tab. Select **Update NASA hotspots hourly** and choose **Run workflow** on main. Uploading the workflow/scripts should also start its first run automatically.
5. Wait for a green successful run. It creates a separate **hotspot-data** branch containing `data/hotspots.json`. No NASA key or personal GitHub token is needed; the workflow uses GitHub's built-in repository token.
6. Let your existing Vercel integration deploy the new main-branch website once. On the website, click **Refresh Data**. The regional section should show a dated NASA export retrieval, observation times and detection locations.

Expected public data address after the first successful Action:
https://raw.githubusercontent.com/shannonluiz78/HazeWatch-SG/hotspot-data/data/hotspots.json

The website reads this public JSON directly, avoiding a website rebuild each hour. `vercel.json` excludes the data branch from automatic deployments; main still deploys normally. Keep the repository public for this approach. The included `data/hotspots.json` is a genuine initial download for local preview/reference; the production website reads the hourly data branch and does not silently fall back to this initial file.

## What changes and when

- The GitHub workflow retrieves NASA's Suomi-NPP VIIRS 375 m Collection 2 near-real-time Southeast Asia 24-hour export at approximately **17 minutes past every hour**. GitHub can delay scheduled jobs; this is not an exact-time guarantee.
- The open website checks the published JSON **every five minutes**, on page load, and when Refresh Data is clicked. GitHub raw-content caching can add a short delay.
- Counts and map points represent nominal/high-confidence satellite detections in the **past 24 hours**, on mainland Sumatra and Indonesian Kalimantan only. Natural Earth country polygons provide geographic filtering; this intentionally excludes neighbouring islands and Malaysian Borneo. Older observations are removed as the page clock advances.
- **Newly listed** means a detection was absent from the previous successful retrieval. It is not proof of a newly started fire. Late satellite processing can introduce older observations; reprocessed records with changed coordinates can also count as newly listed. The first successful retrieval establishes the comparison baseline.
- Existing detections are orange. Newly listed detections are pink with a white outline. Hovering over a desktop point shows its observation time, coordinates, confidence and fire radiative power. A phone-friendly expandable table shows the most recent 12 locations and times.
- Observation and retrieval dates include the year and are shown in **Singapore time (SGT)**. A newer retrieval does not mean NASA has published newer observations. Satellite passes, clouds and processing delays can leave counts unchanged for hours.
- If downloads fail or the export is malformed/outdated, the Action fails and leaves the previous successful JSON intact. The website flags retrievals older than three hours as overdue, and hides them after 24 hours. A failed browser check retains available last-known data with an explicit warning.
- The PM2.5, PSI, wind, selector fixes, guidance colours, portrait and embedded Singapore map are preserved.

## Troubleshooting

- **Workflow missing:** confirm `.github/workflows/update-hotspots.yml` exists on main, rather than only on a test branch or inside a ZIP. GitHub does not extract uploaded ZIPs.
- **Push permission error:** check Settings → Actions → General → Workflow permissions. This workflow requests `contents: write` solely to publish the public data branch. Organisation policies or branch protection rules can override that permission; ensure this bot is permitted to create/update hotspot-data. Do not disable protection on main.
- **Data address is 404:** run the workflow and inspect its logs; the hotspot-data branch must exist and the repository must be public.
- **Unchanged numbers:** compare observation times. An hourly check can retrieve the same NASA observations. New data are limited by satellite passes and NASA processing, not website refresh frequency.
- **Updates stop:** check Actions for failures or a disabled schedule. GitHub may disable scheduled workflows in public repositories after 60 days without repository activity. Re-enable the workflow if this occurs.
- **Local file:** opening the HTML directly may restrict browser requests. Test the deployed HTTPS site or serve the folder locally. The HTML has no embedded fake hotspot readings.

Official references:
- NASA public downloads: https://firms.modaps.eosdis.nasa.gov/active_fire/
- NASA near-real-time data context: https://disasters.nasa.gov/what-we-do/disasters/fires
- GitHub schedule behaviour: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule
- Vercel branch deployment controls: https://vercel.com/docs/project-configuration/git-configuration#git.deploymentenabled

## Validation performed before delivery

Successfully downloaded the current public NASA export and validated its schema, satellite, coordinates, confidence and observation times. Checked geographic counts, duplicate removal, first-run/unchanged/new-arrival comparisons, regional zero counts, stale/malformed feed rejection, browser missing/failed/overdue/expired states, map redraw and selector regression. Local browser preview uses that genuine downloaded JSON; a completed GitHub Action and production deployment remain to be verified after upload.

This package is prepared locally. It has not been uploaded to GitHub or activated on your live site.
