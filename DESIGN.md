---
name: Atmospheric Health Console
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#002113'
  on-tertiary-container: '#009668'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 56px
    fontWeight: '800'
    lineHeight: 60px
    letterSpacing: -0.03em
  display-hero-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  metric-numeral-lg:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.03em
  metric-numeral-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
  data-mono:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-tablet: 1.25rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-tablet: 1.5rem
  margin-desktop: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.875rem
  space-lg: 1.25rem
  space-xl: 1.75rem
---

## Brand & Style

This design system blends governmental environmental precision with consumer biometric technology. The interface treats ambient environmental conditions with the urgency, rigor, and clinical legibility of human vitals. Designed for urban residents, outdoor enthusiasts, vulnerable populations (asthmatics, elderly, parents), and healthcare practitioners, it communicates atmospheric real-time metrics with zero latency or ambiguity.

The aesthetic philosophy fuses **High-Density Utility** with **Tactile Technical Polish**:
- **Information Architecture:** Data surfaces prioritize instantaneous scannability: index values, 1-hour PM2.5 concentrations, and 24-hour PSI figures sit front and center.
- **Visual Restraint:** Non-metric decorative elements are eliminated. Color is functional, reserved strictly for severity classification, critical thresholds, and contextual guidance.
- **Institutional Authority:** Visual patterns evoke precision telemetry dashboards, balanced by the tactile clarity and soft-edge ergonomics of modern hardware-connected health applications.

## Colors

The system uses a crisp, high-contrast light slate canvas as default, anchored by deep slate-navy structural chrome. Hazard-tier signaling follows strict public health conventions, utilizing pure semantic tones across UI tiers.

### Structural Palette
- **Canvas Base:** `#F8FAFC` (Slate 50) establishes a crisp, glare-free backdrop.
- **Surface Elevation 1 (Cards & Modules):** `#FFFFFF` provides clean contrast against the slate canvas.
- **Surface Elevation 2 (Grouped Insets & Data Wells):** `#F1F5F9` (Slate 100).
- **Primary Ink / Structural Chrome:** `#0F172A` (Slate 900) for primary headlines, critical data points, and foundational toolbars.
- **Secondary Ink:** `#475569` (Slate 600) for sub-metrics, operational metadata, and tabular headers.
- **Muted Ink:** `#94A3B8` (Slate 400) for unit annotations (`µg/m³`, `PSI`), disabled states, and chart axes.
- **Subtle Dividers & Outlines:** `#E2E8F0` (Slate 200).

### Air Quality Spectrum Tokens
- **Tier 1 (Good | 0–50 PSI / 0–12 µg/m³):** `#10B981` (Emerald 500) paired with `#ECFDF5` (Surface Tint).
- **Tier 2 (Moderate | 51–100 PSI / 13–55 µg/m³):** `#F59E0B` (Amber 500) paired with `#FFFBEB` (Surface Tint).
- **Tier 3 (Unhealthy | 101–200 PSI / 56–150 µg/m³):** `#F97316` (Orange 500) paired with `#FFF7ED` (Surface Tint).
- **Tier 4 (Very Unhealthy | 201–300 PSI / 151–250 µg/m³):** `#EF4444` (Red 500) paired with `#FEF2F2` (Surface Tint).
- **Tier 5 (Hazardous | 301+ PSI / >250 µg/m³):** `#7F1D1D` (Red 900 / Maroon) paired with `#450A0A` (Deep Contrast Accent).

### Interaction & Utility Tokens
- **Interactive Action (Links, Actionable Selectors):** `#2563EB` (Blue 600).
- **Action Hover / Pressed:** `#1D4ED8` (Blue 700).

## Typography

Typography establishes an engineered, clinical hierarchy. 

### Configuration & Font Features
- **OpenType Feature Activation:** All numerical values, tables, and sensor tickers must enforce `font-feature-settings: "tnum" on, "cv02" on, "cv03" on, "cv04" on`. Tabular lining numbers guarantee horizontal stability during streaming real-time metric updates.
- **Headings (Plus Jakarta Sans):** Applied to top-tier status callouts, view identifiers, and zone names (e.g., "Central", "North-East"). The tight letter-spacing yields a confident, modern technology brand posture.
- **Data & Text Body (Inter):** Applied across analytical outputs, data grids, affiliate specs, advisory copy, and micro-labels. Small labels utilize uppercase casing combined with widened tracking (`+0.04em`) to ensure readability on mobile screens under direct sunlight.

## Layout & Spacing

The layout adheres to an information-dense, structured grid designed to surface critical data without unnecessary scrolling.

### Grid Architecture
- **Mobile (<768px):** 4-column fluid layout; 16px outer margin; 16px gutters. Regional metrics stack into segmented swipeable cards or compact vertically sequenced blocks.
- **Tablet (768px - 1024px):** 8-column layout; 24px outer margins; 20px gutters. Map view and primary index sit parallel in a 5:3 column split.
- **Desktop (>1024px):** 12-column layout; 32px outer margins; 24px gutters; maximum content container width of 1440px. 
  - **Left Rail (4 cols):** Sticky National Air Quality summary, acute health advisories, personalized sensitive-group toggles.
  - **Center Canvas (5 cols):** Dynamic interactive regional maps, hourly temporal scrubbers, 24-hour pollutant breakdown grids.
  - **Right Rail (3 cols):** Action modules, protective inventory/affiliate procurement (N95 filters, medical HEPA devices), and telemedicine queues.

### Density Strategy
Component padding remains tight: card interiors use `space-md` (14px) or `space-lg` (20px), maximizing above-the-fold telemetry density. Elements within metric blocks use micro-steps (`space-xs` to `space-sm`) to lock labels to their respective scalar values.

## Elevation & Depth

Visual hierarchy uses clean surface stacking, fine hairline borders, and subtle tinted ambient occlusion rather than heavy drop shadows. This preserves daylight legibility and maintains clinical authority.

### Surface Hierarchy
- **Level 0 (App Canvas):** Base `#F8FAFC`.
- **Level 1 (Surface Cards & Visual Shelves):** Solid `#FFFFFF` enclosed in a 1px solid border (`#E2E8F0`).
- **Level 2 (Active/Selected Panels, Tooltips, Floating Menus):** Pure `#FFFFFF` elevated via:
  `box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.06), 0 2px 6px -1px rgba(15, 23, 42, 0.04);`
  Enclosed with border `rgba(15, 23, 42, 0.08)`.
- **Level 3 (Urgent Critical Alert Banners):** When PSI exceeds safe parameters, banners utilize low-opacity background saturations with left-edge solid indicator accents (4px border-left in the corresponding hazard hex).
- **Interactive Element Elevation:** Cards do not float up on hover; instead, interactive cards respond through a 1px border shift to `#94A3B8` and a subtle inner ambient glow (`box-shadow: 0 0 0 1px #2563EB`).

## Shapes

The design system adopts a balanced roundedness (`0.5rem` / `8px` default radius) to balance consumer software friendliness with computational rigor.

### Radius Distribution
- **Form Controls, Micro Badges & Action Chips:** `rounded-md` (`0.375rem` / `6px`) ensures sharp spatial cohesion within dense data tables.
- **Standard Telemetry Cards, Metrics Panels, Map Modules:** `rounded` (`0.5rem` / `8px`) cleanly defines content islands without wasting canvas corners.
- **Dialogs, Drawers & System Modals:** `rounded-lg` (`1rem` / `16px`) creates distinct structural hierarchy for focused overlay experiences.
- **Pill Badges:** Fully circular (`rounded-full` / `9999px`) reserved exclusively for real-time sensor status ("LIVE", "OFFLINE") and categorical severity chips ("MODERATE", "UNHEALTHY").

## Components

### Status Chips & Hazard Indicators
- **Architecture:** Compact height (24px) consisting of an optional 6px pulsing sensor dot, uppercase `label-sm` text, and tabular value indicators.
- **Color Mapping:** Background tint at 12% opacity of the hazard color, text rendered in dark-mode equivalent or high-contrast shade of that respective hazard spectrum, and a solid 1px border at 20% opacity.

### Telemetry Cards
- **Structure:** 1px solid `#E2E8F0` border, `#FFFFFF` background, 14px internal padding.
- **Header:** Secondary label (`label-sm`, uppercase, `#64748B`) paired with a micro information-trigger icon.
- **Metric Readout:** Tabular numeral (`metric-numeral-lg`, `#0F172A`) paired with a baseline-aligned unit denominator (`µg/m³`, `body-sm`, `#94A3B8`).
- **Footer:** Historical 12-hour micro sparkline (height: 24px) rendered with crisp 1.5px paths in the active hazard color.

### Data Tables & Pollutant Breakdowns
- **Row Heights:** 36px condensed rows.
- **Dividers:** 1px solid hairline borders (`#F1F5F9`).
- **Alignment:** Alphanumeric parameter names align left; all sensor measurements, delta values, and hazard grades strictly align right with tabular figures enabled.

### Alert Banners
- **Severe Hazard State:** Positioned at viewport top or card head. Full width, `#FEF2F2` background, bordered with `#FCA5A5`, featuring an assertive status indicator (`#EF4444`) and direct public health advice (e.g., "Avoid prolonged outdoor exertion. High PM2.5 detected in Western Region.").

### Input Fields & Segmented Controls
- **Segmented Region Switches:** Container `#F1F5F9`, 4px internal padding. Selected segment employs `#FFFFFF`, sharp `rounded-md`, and a discrete ambient drop shadow.
- **Text & Filter Inputs:** Height 36px, `#FFFFFF` fill, 1px `#E2E8F0` border, `#0F172A` text, transitions to a 1.5px `#2563EB` border focus ring with zero offset spread.

### Action & Contextual Utility Modules (Affiliate / Health Integration)
- **Visual Distinction:** Distinct from primary public health telemetry via subtle slate-cool styling. Card background `#F8FAFC`, surrounded by a deliberate dashed or muted hairline border (`#CBD5E1`).
- **Metadata Framing:** Explicit micro-badge labeled "HEALTH COUNTERMEASURE" or "RECOMMENDED HARDWARE" (`label-sm`, `#64748B`).
- **Interactive Triggers:** High-efficiency button layout with primary CTA (`#0F172A` background, `#FFFFFF` text, `rounded-md`, 32px height) providing instant external handoff to validated stockists, pharmacy portals, or clinical booking engines.