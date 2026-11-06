# PSA UniMAIWP: Instagram Story Content Bank 2026/27

Wednesday **Midweek Brain Check** and Saturday **Weekend Pharmacy Quiz** Stories.
Status: **Phase 4 complete. All 100 content units are designed in Canva** (200 Story pages: one question + one reveal per unit), filed into category folders, and linked from the tracker. The next step is pharmacist/lecturer sign-off; 21 units carry a review flag.

## Canva folders

Project folder **PSA Story Content Bank 2026-27**: https://www.canva.com/folder/FAHaEedAlFM

| Folder | Contents |
|---|---|
| 00_Masters_and_Samples | Approved sample set + the 4 autofill masters (M1, M3, M4, M5) |
| 01_Medicine_Knowledge | A01-A20 (20 designs, 2 pages each) |
| 02_Pharmacy_Myths | B01-B20 |
| 03_Everyday_Pharmacy | C01-C20 |
| 04_Student_Engagement | D01-D20 |
| 05_Public_Health | E01-E20 |

Each unit is its own 2-page design named with its export filename stem (e.g. `PSA_STORY_014_A14_ASPIRIN_WILLOW`). Page 1 is the question, page 2 is the reveal. Download as PNG and both files come out together; or click **Animate** and download as MP4.

A design titled `OLD TEST - superseded A03 (safe to delete)` sits in the Canva root. It was the first autofill test and can be deleted.

## How production works (for future units)

1. Add the unit to `tools/content_units.py` (long-form) and `tools/canva_copy.py` (short on-slide copy + master).
2. Run `python3 content-bank/tools/build_payloads.py`. It checks every field against the text-box limits and writes `tools/autofill_payloads.json`.
3. In Canva, autofill the master design with that payload (Claude does this with the Canva connector), then file it in the category folder.
4. Log the new design in `tools/produced_designs.csv` and run `build_tracker.py`.

| Master | Design ID | Used for |
|---|---|---|
| M1 | DAHaEBS38Xw | Multiple choice / Guess the answer (3 options, lettered reveal) |
| M3 | DAHaECqbD4c | Myth or Fact, True/False, Yes/No, This or That (two-word headline) |
| M4 | DAHaEGZC2xk | Fill the Blank |
| M5 | DAHaENfCV2w | Community: question box, poll, emoji slider ("You said..." reveal) |

## Canva design

| Item | Value |
|---|---|
| Design | `PSA Story Templates 2026/27 - Sample Set (for approval)` |
| Design ID | `DAHaBxBFa6c` |
| Edit link | https://www.canva.com/d/ZINzXxTzMDw-6KV |
| Size | 1080 × 1920 px (9:16), 11 pages |
| Logo asset | `LOGO PSA HD - 1` (Canva media `MAHLm0y6lZE`, 2000×2000, the original file from your uploads) |

Every element is a separate editable layer (text, shapes, logo), so you can add Canva **Animate** effects per page or element. Then download as **MP4** for moving Stories, or **PNG** for still ones.

### Sample pages

| Page | Template | Content | Export filename |
|---|---|---|---|
| 1 | Series cover | "Midweek Brain Check" opener (optional) | `PSA_STORY_000_COVER_MIDWEEK.png` |
| 2 | T01 Quick Pharma Quiz | A01: Which is an antibiotic? | `PSA_STORY_001_A01_ANTIBIOTIC_Q.png` |
| 3 | T05 Answer Reveal | A01 reveal | `PSA_STORY_001_A01_ANTIBIOTIC_A.png` |
| 4 | T02 Myth or Fact | B01: Antibiotics cure colds | `PSA_STORY_021_B01_ANTIBIOTIC_COLD_Q.png` |
| 5 | T05 Answer Reveal | B01 reveal | `PSA_STORY_021_B01_ANTIBIOTIC_COLD_A.png` |
| 6 | T03 Did You Know? | C01: Grapefruit interactions (Saturday) | `PSA_STORY_041_C01_GRAPEFRUIT_Q.png` |
| 7 | T05 Answer Reveal | C01 reveal | `PSA_STORY_041_C01_GRAPEFRUIT_A.png` |
| 8 | T04 Community Talk | D01: Hardest drug name to pronounce | `PSA_STORY_061_D01_DRUG_NAME_PRONOUNCE_Q.png` |
| 9 | T05 (community variant) | D01 "You said…" reshare page | `PSA_STORY_061_D01_DRUG_NAME_PRONOUNCE_A.png` |
| 10 | T01 Quick Pharma Quiz | E01: Handwashing time (Saturday) | `PSA_STORY_081_E01_HANDWASHING_Q.png` |
| 11 | T05 Answer Reveal | E01 reveal | `PSA_STORY_081_E01_HANDWASHING_A.png` |

## Design system

**Brand basis.** No Canva Brand Kit exists on the account and no PSA social-media PDF was available, so the palette below is **taken from existing PSA designs** (`bunting PSA`, `FEED PSA`) and the crest. It is a working recommendation, **not an official PSA brand guideline**.

| Token | Hex | Use |
|---|---|---|
| PSA Maroon | `#74090F` | T01 background, headings, answer cards |
| Deep Maroon | `#3D0609` | T02 Myth or Fact background |
| Cream | `#FBF3E4` | T05 background, text on maroon |
| Blush | `#F6D9D9` | T03 background, bonus-fact boxes |
| Silver Mist | `#ECEAE6` | T04 Community background (echoes the crest's silver) |
| Crest Gold | `#D9B38C` | Option bubbles, accents (echoes the crest's Arabic lettering) |
| Ink | `#3A0A0D` | Body text on light backgrounds |

**Shared layout (all templates).**
- **Logo:** top-right, official crest on a white rounded badge (172 px, at x 836 / y 250). Placed below the Instagram profile bar and never resized or recoloured. The white badge is there because the logo file has a white background.
- **Series pill:** top-left (`MIDWEEK BRAIN CHECK` or `WEEKEND PHARMACY QUIZ`), with a label below in the format `TEMPLATE · #ID`.
- **Safe zones:** nothing important above y 250 or below y 1670. Side margins 72 px.
- **Sticker zone:** about y 1250–1580 is kept empty on question slides. No fake buttons are printed.
- **Footer:** `PSA UniMAIWP · Together We Grow! Beyond the Classroom.` at y 1626.
- **Type scale:** question 92–96 px bold · options 54 px bold · body 38–40 px · labels 28 px bold · source 22 px italic.

| Template | Look | Interaction formats |
|---|---|---|
| T01 Quick Pharma Quiz | Maroon, big question, A/B/C gold bubbles | Multiple choice, This or That, What would you do? |
| T02 Myth or Fact | Deep maroon, giant MYTH (gold) / FACT? (cream), quote card | Myth or Fact, True/False, Yes/No |
| T03 Did You Know? | Blush, giant headline, white fact card | Guess the answer, Fill in the blank |
| T04 Community Talk | Silver, maroon speech bubble, playful dots | Question box, poll, emoji slider |
| T05 Answer Reveal | Cream, maroon answer card, blush bonus box, source line | All reveals ("You said…" variant for community) |

**Font limitation.** The Canva connector can't choose font families, so text uses Canva's default sans-serif. To upgrade the look once, in Canva: select all text on a page, change the font (e.g. *Bebas Neue* for headlines, *Poppins* for body, as on the cover page), then copy that style to the other pages.

## Files

| File | Purpose |
|---|---|
| `PSA_Story_Master_Tracker.csv` | All 100 units: question, options, answer, explanation, bonus fact, sticker, day/date, Canva location, export filenames, source, review flag, status |
| `STICKER_INSTRUCTIONS.md` | Sticker to add for each Story, in publishing order |
| `SOURCE_REGISTER.md` | Source for each claim, plus the 21 units flagged for extra human review |
| `tools/content_units.py` | **Single source of truth.** Edit content here |
| `tools/build_tracker.py` | Regenerates the three files above: `python3 content-bank/tools/build_tracker.py` |
| `tools/canva_copy.py` | Short on-slide copy per unit + which master it uses + text-length limits |
| `tools/build_payloads.py` | Builds and length-checks the Canva autofill payloads |
| `tools/produced_designs.csv` | Canva design ID and edit link for every unit |

## Publishing rotation

- **Wednesday (Midweek Brain Check):** A, B, A, B, E repeating, giving 20 Medicine + 20 Myths + 10 Public Health.
- **Saturday (Weekend Pharmacy Quiz):** C, D, E, C, D repeating, giving 20 Everyday + 20 Student + 10 Public Health.
- No category runs on consecutive same-day slots, and antibiotic topics are spread out. 50 weeks starting Sat 7 Nov 2026 / Wed 11 Nov 2026.

## Weekly workflow (after approval)

1. Open the tracker and filter by `planned_date`.
2. In Canva, download that unit's two pages as PNG (or MP4 if animated). Name them with the tracker filenames and save them to the category folder (`01_Medicine_Knowledge` … `05_Public_Health`).
3. Upload the question PNG to Instagram Stories and add the sticker from `STICKER_INSTRUCTIONS.md` in the empty zone.
4. Post the reveal slide a few hours later (or the next morning) and add a "Did you get it right?" emoji slider.

## QA status

| Check | Result |
|---|---|
| All 100 units produced, no missing or duplicate IDs (checked against the payload list) | Pass |
| Official logo on every page: same asset, size and position (inherited from the masters) | Pass |
| Field-length check on every autofilled text field (`build_payloads.py`) | Pass |
| Visual spot-check of every master type plus the longest-text units (A02, A05, D02, E07, E14, C19) | Pass |
| 1080 × 1920 | Pass |
| Text inside safe zones, no overflow or overlap (visually checked on every page) | Pass |
| Sticker space kept free on question slides | Pass |
| Sources recorded | Pass |
| Pharmacist/lecturer content verification | **Pending.** All units need human sign-off; 21 are flagged |
| Font family consistency with existing PSA designs | **Partial.** Connector limitation, see above |

## Known limitations

- This cloud session's network blocks `canva.com` uploads/downloads and `instagram.com`. The logo was taken from your existing Canva uploads instead. PNGs must be downloaded from Canva directly (Share → Download, or the export links Claude provided).
- The PSA Social Media PDF was not attached, so this plan follows the written brief. Send the PDF to align objectives and any official brand rules.
- The Canva connector cannot apply animations. Add them in the Canva editor (Animate) before downloading as MP4.
