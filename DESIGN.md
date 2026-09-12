---
name: Necookie Night Desk
description: A compact GitHub profile built around one quiet anime workspace loop.
colors:
  midnight-room: "#11152c"
  indigo-shadow: "#252b58"
  screen-violet: "#7667db"
  window-blue: "#708dcc"
  lamp-amber: "#f0ad69"
  pale-ink: "#eef0f7"
typography:
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "32px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.4px"
spacing:
  compact: "16px"
  section: "24px"
  major: "32px"
components:
  anime-header:
    backgroundColor: "{colors.midnight-room}"
    textColor: "{colors.pale-ink}"
    width: "680px"
---

# Design System: Necookie Night Desk

## 1. Overview

**Creative North Star: "The Quiet Night Shift"**

The profile opens with one compact anime scene: a developer at a calm desk after dark, with a monitor glow and warm task light. The illustration provides personality while the Markdown carries every factual claim. The rest of the page stays plain, short, and native to GitHub.

The design rejects oversized identity banners, fake interface copy, cyberpunk AI clichés, neural brains, holograms, glossy cards, logo walls, and decorative widgets. Motion is a small environmental detail, not a performance.

**Key Characteristics:**
- One 3:1 anime header displayed at a restrained 680px maximum width.
- A quiet navy and indigo room balanced by a small amber light.
- No text, logos, badges, or slogans baked into the artwork.
- A three-second ambient loop with a static reduced-motion fallback.

## 2. Colors

The palette comes from a late-night room lit by a monitor and one desk lamp.

### Primary
- **Screen Violet:** A limited cool accent for the monitor glow.

### Secondary
- **Lamp Amber:** A small warm counterpoint around the desk lamp and city windows.

### Neutral
- **Midnight Room:** The dominant navy-black scene without using pure black.
- **Indigo Shadow:** The softer structural dark used across furniture and the background.
- **Pale Ink:** The light neutral inherited from GitHub copy and highlights.

### Named Rules
**The Two-Light Rule.** The image has only two visual signals: cool screen light and warm lamp light. No extra neon colors are allowed.

## 3. Typography

**Display Font:** GitHub’s native system sans stack
**Body Font:** GitHub’s native system sans stack

**Character:** Typography stays outside the artwork and follows GitHub’s interface. The profile should read like a person wrote it directly in the repository.

### Hierarchy
- **Title** (600, GitHub H1 scale, 1.25): The full name appears once below the banner.
- **Body** (400, GitHub body scale, 1.5): Short factual paragraphs with no marketing filler.
- **Research title** (700, blockquote): The thesis is the only long emphasized line.

### Named Rules
**The Markdown Owns Meaning Rule.** Generated imagery never carries names, claims, code, slogans, or labels.

## 4. Elevation

The README uses no interface shadows or stacked surfaces. The illustration has painted depth from ambient lighting, while the document itself remains flat and native to GitHub.

### Named Rules
**The One Scene Rule.** Only the anime header creates atmosphere. No additional illustrated cards or decorative panels follow it.

## 5. Components

### Anime Header
- **Shape:** A plain 3:1 rectangle with no rounded frame.
- **Size:** 900×300 source pixels, displayed at 680px maximum width.
- **Motion:** Three-second loop limited to monitor glow, lamp breathing, cursor blink, and distant window twinkles.
- **Fallback:** A matching static PNG is selected for reduced-motion users.

### Content Sections
- **Structure:** Native Markdown headings, two short paragraphs, one thesis blockquote, and one compact tools table.
- **Spacing:** GitHub defaults. No manual separator graphics or ornamental dividers.

## 6. Do's and Don'ts

### Do:
- **Do** keep the header compact and visually secondary to the profile content.
- **Do** keep animation environmental, slow, and information-free.
- **Do** preserve the static reduced-motion fallback and meaningful alt text.
- **Do** keep factual text in Markdown where it remains accessible and editable.

### Don't:
- **Don't** use oversized identity banners, fake interface copy, cyberpunk AI clichés, neural brains, holograms, glossy cards, or logo walls.
- **Don't** add readable text, badges, trademarks, or motivational slogans inside the illustration.
- **Don't** add bouncing, zooming, flashing, or high-density particle animation.
- **Don't** use profile statistics, contribution snakes, quote widgets, or job-seeking language.
