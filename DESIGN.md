# Design system: Shalome & Tanmay save-the-date

Written in the DESIGN.md format (see VoltAgent/awesome-design-md) so any design agent knows how this page should look before changing it.

## Overview
A warm, celebratory save-the-date for friends, opened on a phone. The painted Goa garden scene leads and the interface stays out of the way. Soft, airy, hand-made. Never corporate, never busy.

## Rules that do not change
- The painted scenery is fixed: trees, house, couple, blue sky, sea. Detail may be added on top, nothing removed.
- Do not cover the painted birds.
- Existing copy stays; new wording needs the owner's approval.
- Order: swipe, video, scratch the cloud (same screen as the video), card.

## Colors
| Token | Value | Use |
|---|---|---|
| `--sky` | `#d2dde9` | screen fallback behind artwork |
| `--sky-soft` | `#e6edf4` | page background, cloud plate |
| `--paper` | `#f7f1e3` | warm cream (card border, petals) |
| `--sage` | `#5f6f3f` | the date |
| `--sage-deep` | `#4c5a31` | labels, icons, arrow |
| `--ink` | `#33422a` | body and prompt text |
Clouds are white with a cool blue shadow (`rgba(70,96,130,.2-.28)`). Petals fade from ivory to `#f4c862`.

## Typography
Cormorant (self-hosted, 500 and 600, normal and italic), serif fallback Georgia. Prompts and hints are italic 600 at 1.1-1.3rem. Labels are uppercase, 600, letter-spaced .24em. The date is 600 at `clamp(1.35rem, 6.6vw, 1.95rem)`. Text over the artwork gets a soft pale glow, never a hard shadow.

## Layout
Full-screen stacked screens (`100dvh`), mobile first, content column up to 520px wide. Safe-area insets respected. The cloud is `min(90vw, 420px)`. Small clouds sit beside the prompt and right of the date, clear of the birds.

## Elevation and shape
Flat, with soft drop shadows on clouds only. Round 44px icon buttons with frosted white backgrounds (replay bottom-left, music bottom-right).

## Motion
- Easing: `--ease-out` for arrivals, `--ease-soft` for fades.
- Intro swipe-right with snapback, video, then the cloud layer fades in over its last frame (1.2s).
- Cloud sheen until first touch; small clouds drift slowly; petals fall from the left tree.
- The date reveal glides to the card; the card settles in once; music fades in over 3s after the date shows.
- `prefers-reduced-motion`: all animation and glides off.

## Accessibility
Intro and cloud are keyboard operable (Enter). Touch targets 44px. Hidden layers are `inert`. The scratch hint is `aria-live`.

## Do and don't
Do keep it light, warm and quiet. Don't add heavy gradients, new colors, dark mode, or UI chrome that competes with the painting.
