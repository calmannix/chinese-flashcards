# Changelog

## 2026-03-10

### Fixed

- **Card selection randomisation**: slice was applied before shuffle in both word and phrase sessions, causing the same subset of cards (always the oldest-added) to be selected when a card limit was set. Shuffle now runs first so the limit picks a truly random subset each session.
- **Smart Shuffle card ordering**: final selection was returned as hard → good → easy groups, making difficulty predictable by position. A final shuffle now interleaves all three difficulty tiers.

---

## 2026-03-06

### Fixed

- Grade buttons (Hard/Good/Easy) not responding in review sessions — `stats.dailyLog` was undefined when loaded via server cache, causing a TypeError that silently blocked grading. Again worked because it returns before touching stats.
- Mastery distribution Easy threshold lowered from 2.8 to 2.6 — previously required 3 consecutive Easy grades before a card counted as Easy.

### Added

- **Phrase activity modes**: Translate (English shown, recall Chinese), Reading (characters only, recall meaning), and Complete (Memorise → Translate → Reading in sequence). Replaces the old Reveal mode.
- Keyboard hints now context-aware: shows only "Space Flip" before reveal, full grade shortcuts after.
- CN→EN flashcards auto-open radical breakdown on reveal for character recognition focus.

### Changed

- CN→EN flashcards no longer show pinyin on the question side — forces character recognition.
- Mastery distribution label changed from "Mastery distribution" to "How well you know your words".

### Removed

- Speech/audio feature removed entirely: speak buttons, auto-play toggle, P keyboard shortcut, and all SpeechSynthesis API code. The feature was unreliable.

---

## 2026-03-05

### Added

- **Keyboard shortcuts** for review sessions: Space to flip, 1-4 to grade, P to speak. Hint row shown below each card. Adapts to binary grading modes (Complete Learning test phases, Phrase Reveal).
- **Dashboard** on the Home screen with five components:
  - Streak counter (consecutive review days, green/grey state)
  - Daily target progress bar with editable target (default: 20)
  - 90-day activity heatmap (4 intensity levels)
  - 8-week accuracy trend line (% Good + Easy grades)
  - Mastery distribution bar (Hard / Good / Easy split)
- **Radical decomposition** on flashcards: magnifying glass button shows character breakdown into radicals with English meanings. "Also in your vocab" lists related words sharing the same components. Data from Make Me a Hanzi (9,490 characters, 1,787 radical meanings).
- **Daily review log**: aggregated stats per day (total, again, hard, good, easy). Powers the dashboard charts and streak tracking.
- **Data version migration**: stats object includes 'dataVersion' field. Old data auto-migrates on load with safe defaults.
- Toast notification when daily target is reached.

### Changed

- Daily target text reads "completed today" instead of "cards today" to clarify it counts successful grades only (Again re-queues without counting).

### New files

- 'radicals.js' (878 KB): radical decomposition and Kangxi radical meanings data
- 'generate_radicals.py': one-time script to regenerate radicals.js from Make Me a Hanzi dictionary.txt
