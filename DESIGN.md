---
name: Necookie Profile Field Notes
description: A theme-aware GitHub profile that reads like a concise engineering notebook.
colors:
  light-paper: "#f7f7f2"
  dark-paper: "#171b18"
  light-ink: "#1e2521"
  dark-ink: "#edf1eb"
  light-rule: "#c9cec6"
  dark-rule: "#414a43"
  signal-rust-light: "#c56447"
  signal-rust-dark: "#dc8564"
  light-wash: "#e7ece5"
  dark-wash: "#222923"
typography:
  display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "58px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-2px"
  body:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "normal"
  label:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.8px"
spacing:
  edge: "40px"
  note: "56px"
  section: "72px"
components:
  field-note-graphic:
    backgroundColor: "{colors.light-paper}"
    textColor: "{colors.light-ink}"
    typography: "{typography.display}"
    padding: "40px"
  research-map-graphic:
    backgroundColor: "{colors.light-paper}"
    textColor: "{colors.light-ink}"
    typography: "{typography.label}"
    padding: "40px"
---

# Design System: Necookie Profile Field Notes

## 1. Overview

**Creative North Star: "The Maintained Field Notebook"**

This is a brand surface inside GitHub, designed for a visitor who is scanning between repositories and wants a fast, credible read on the person behind them. A defined perimeter, field labels, and deliberate diagram notation do the visual work. The page stays left-aligned because GitHub is the environment, not a canvas to overpower.

The system is deliberately quiet. It rejects profile-README template stacks, giant logo walls, scrolling widgets, contribution snakes, stats badges, quote widgets, watermarked typing GIFs, and social/contact call-to-actions. It also rejects generic AI imagery, neural brains, glossy cards, gradients, fan art, inflated claims, and job-seeking language.

**Key Characteristics:**
- Structured, factual, and spatially calm.
- Original vector notation in place of stock or AI-generated imagery.
- A tiny geometric cookie-cat seal supplies recognition without mascot excess.
- Light and dark modes are separate compositions with matched hierarchy and contrast.
- Desktop and mobile SVGs are separate compositions, selected with theme and a 600px media condition.

## 2. Colors

The palette behaves like paper, ink, drafting rules, and one small signal color.

### Primary
- **Signal Rust:** Reserved for the tiny cookie-cat seal, diagram glyphs, and directional accents. It never becomes a surface or a decorative wash.

### Neutral
- **Paper:** The calm field behind the light artwork; the dark counterpart is a soft charcoal-green rather than pure black.
- **Ink:** High-contrast copy and structural lines in both themes.
- **Rule and Wash:** Subordinate grid lines and alternating diagram fills that organize without reading as cards.

### Named Rules
**The One Signal Rule.** Signal Rust belongs only to meaningful marks: a geometry, a chart bar, a route, or an arrow. It is not a general highlight color.

## 3. Typography

**Display Font:** Arial, Helvetica, sans-serif
**Body Font:** Arial, Helvetica, sans-serif
**Label/Mono Font:** ui-monospace, SFMono-Regular, Menlo, Consolas, monospace

**Character:** Direct system text, not a simulated terminal. The sans carries names and explanations; the monospace face acts only as a margin label and measurement language.

### Hierarchy
- **Display** (700, 58px, 1): Used once in the identity graphic for the full name.
- **Headline** (700, 16px, 1.2): Used inside research-map stages to make each node scannable.
- **Body** (400, 17px, 1.45): Used for README notes, with paragraphs kept comfortably short.
- **Label** (400, 12px, 0.8px tracking, uppercase): Used for graphic metadata, versioning, and diagram coordinates.

### Named Rules
**The No Costume Rule.** Monospace never writes the personal narrative. It only records the field-note metadata around it.

## 4. Elevation

This system uses no shadows. Depth comes from the outer frame, quiet drafting rules, and alternating flat washes in the research map. If an element needs attention, it earns it through placement, weight, or the signal color, never simulated elevation.

### Named Rules
**The Flat Evidence Rule.** Everything stays flat and inspectable. No glass, glow, blur, or glossy-card treatment is permitted.

## 5. Components

### Cards / Containers
- **Corner Style:** Square, no radius.
- **Background:** Paper or dark paper, with a restrained wash only for alternate diagram stages.
- **Shadow Strategy:** None.
- **Border:** A single ink perimeter and optional fine drafting rules.
- **Internal Padding:** A 40px graphic edge, scaled naturally by the SVG viewBox.

### Navigation
- **Style:** None. The README relies on GitHub navigation and simple Markdown section headings.

### Field-Note Graphic
The profile identity graphic has wide and narrow compositions. The desktop version uses an outer perimeter, dashed datum lines, descriptive margins, and an original cookie-cat seal. The mobile version stacks the name, role, thesis-oriented systems note, seal, and affiliation labels. Both respond to theme choice with separate source SVGs rather than inverted CSS.

### Research Map
The research graphic is a five-stage conceptual flow. The desktop version reads left to right; the mobile version turns the same stages into a vertical field-note flow. Every stage has a number, text label, distinct glyph, and connecting arrow, so its sequence remains legible without color.

## 6. Do's and Don'ts

### Do:
- **Do** use the paper, ink, rule, wash, and Signal Rust roles exactly as defined in the frontmatter.
- **Do** keep profile content left-aligned, short, and specific to actual work.
- **Do** label the thesis map as conceptual and avoid implementation claims it cannot substantiate.
- **Do** provide paired light and dark SVGs with equivalent readable content and meaningful alt text.
- **Do** use the dedicated mobile source below 600px, not a shrunken desktop composition.

### Don't:
- **Don't** use profile-README template stacks, giant logo walls, scrolling widgets, contribution snakes, stats badges, quote widgets, watermarked typing GIFs, or social/contact call-to-actions.
- **Don't** use generic AI imagery, neural brains, glossy cards, gradients, fan art, inflated claims, or job-seeking language.
- **Don't** render existing Ghibli, soot, or sakura imagery.
- **Don't** use a colored side stripe, rounded SaaS cards, pure black, pure white, or decorative glass effects.
