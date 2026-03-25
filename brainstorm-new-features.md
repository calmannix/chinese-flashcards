# 日日 (Riri) feature brainstorm

**Product**: Standalone macOS Chinese vocabulary trainer with SM-2 spaced repetition
**Target user**: Personal Chinese language learner on macOS
**Constraints**: Offline-first, no frameworks, privacy-focused, minimal dependencies

---

## Perspective 1: Product Manager

Focus: market fit, value creation, differentiation.

### PM-1: Stroke order writing practice
Add an interactive canvas where users trace characters stroke by stroke. Validate each stroke against correct order data. Skritter charges $15/month for this. Building it into Riri gives a free, offline alternative with a clear competitive edge.

### PM-2: HSK level integration
Tag vocabulary by HSK level (1-6 under the new HSK 3.0 standard). Let users filter reviews, track progress, and set goals per level. HSK alignment turns Riri from a general flashcard app into a structured exam prep tool.

### PM-3: Sentence context cards
Show each word inside a full example sentence during review. Sentence-level recall builds fluency faster than isolated word recall. Taalhammer and Clozemaster both differentiate on this approach.

### PM-4: Daily streak and review targets
Track consecutive review days and daily card targets. Display a streak counter on the home screen. Streaks drive habit formation: Duolingo attributes 80% of retention to its streak mechanic.

### PM-5: Radical decomposition view
Break each character into its component radicals with meanings. Show how radicals combine to form the character. This helps users build pattern recognition and memorise new characters faster.

---

## Perspective 2: Product Designer

Focus: user experience, onboarding, engagement.

### UX-1: Guided first-run experience
Walk new users through adding their first 5 words, running a review session, and hearing pronunciation. The current app drops users on an empty home screen with no direction.

### UX-2: Progress dashboard with visual charts
Replace the plain stat counters with a visual dashboard: cards due today, weekly review heatmap (like GitHub's contribution graph), accuracy trends over time, and mastery distribution across lessons.

### UX-3: Dark mode
Add a dark theme toggle. The current bright white/blue design causes eye strain during evening study sessions. Most learning apps support dark mode.

### UX-4: Keyboard-first review flow
Map grading to keyboard shortcuts (1-4 for Again/Hard/Good/Easy, Space to flip). Power users can blitz through reviews without touching the mouse. Anki's keyboard flow is one of its strongest retention features.

### UX-5: Card preview on hover in word list
When hovering over a word in the list view, show a mini flashcard preview with pinyin, tone colours, and next review date. Reduces clicks needed to check individual word status.

---

## Perspective 3: Software Engineer

Focus: technical capabilities, architecture improvements, platform reach.

### ENG-1: Character stroke SVG renderer
Use open-source stroke order data (e.g., Make Me a Hanzi dataset) to render animated stroke sequences as SVGs. No external dependencies needed: parse JSON stroke data and draw paths on a canvas element.

### ENG-2: Offline PWA with service worker
Wrap the app as a Progressive Web App. Register a service worker to cache all assets. This removes the Python server dependency entirely and lets the app run on any platform with a browser (including iOS and Windows).

### ENG-3: SQLite via WASM for data storage
Replace localStorage + JSON file with sql.js (SQLite compiled to WebAssembly). Enables proper querying, indexing, and scales beyond localStorage's 5MB limit. Data exports remain simple JSON.

### ENG-4: Pluggable TTS with local model fallback
Integrate a lightweight local TTS model (e.g., Piper TTS via WASM) as fallback when Web Speech API voices sound robotic. Ships a small Chinese voice model (~20MB) for consistent, natural pronunciation.

### ENG-5: Modular JS architecture
Split the 3,181-line index.html into ES modules: data layer, SM-2 engine, UI components, dictionary, and TTS. Use native ES module imports (no bundler needed). Makes the codebase maintainable and testable.

---

## Top 5 prioritised ideas

### 1. Keyboard-first review flow (UX-4)

**Why first**: Zero new dependencies. Delivers immediate value for the primary use case (reviewing cards). Can ship in an afternoon. Every power user expects this.

**Key assumptions to test**:
- Users review cards daily (validate via session frequency data)
- Mouse-to-keyboard switching slows review sessions measurably

**Effort**: Small (event listeners + key mapping)

---

### 2. Stroke order writing practice (PM-1 + ENG-1)

**Why second**: The single biggest feature gap compared to paid competitors. Transforms Riri from "another flashcard app" into a writing practice tool. Make Me a Hanzi provides free, open-source stroke data for 9,000+ characters.

**Key assumptions to test**:
- Users want to write characters, not only recognise them
- SVG stroke rendering performs well in-browser without a framework

**Effort**: Medium (stroke data integration + canvas drawing + validation logic)

---

### 3. Progress dashboard with visual charts (UX-2)

**Why third**: The data already exists in the SM-2 card objects (review dates, ease factors, intervals). Surfacing it visually creates motivation loops. A heatmap and accuracy chart take a session from "I reviewed 20 cards" to "I've studied 15 days straight and my accuracy rose 12%."

**Key assumptions to test**:
- Visual progress motivates continued use more than raw numbers
- Canvas/SVG charts render acceptably without a charting library

**Effort**: Medium (data aggregation + chart rendering)

---

### 4. Radical decomposition view (PM-5)

**Why fourth**: Radicals are the building blocks of Chinese literacy. Showing decomposition during review helps users see patterns across characters. Free radical databases exist (CJK Decomposition Data). This adds depth without changing the core review loop.

**Key assumptions to test**:
- Users find radical breakdowns helpful vs. distracting during review
- Decomposition data covers the user's vocabulary adequately

**Effort**: Medium (data source integration + UI component)

---

### 5. Daily streak and review targets (PM-4)

**Why fifth**: Simple to build, proven to drive retention. Store a streak counter and daily target in the existing data model. Display prominently on the home screen. Pair with the progress dashboard later for compounding effect.

**Key assumptions to test**:
- A streak counter motivates a solo learner (no social pressure)
- Users prefer gentle nudges over gamification pressure

**Effort**: Small (date tracking + UI display)

---

## Ideas deferred for now

| Idea | Reason to defer |
|------|-----------------|
| Offline PWA (ENG-2) | High value but large effort; revisit once core features stabilise |
| Modular JS (ENG-5) | Internal quality improvement; do incrementally as you touch files |
| SQLite via WASM (ENG-3) | Current storage works fine at personal scale; premature optimisation |
| Guided onboarding (UX-1) | Only matters for new users; the app has one user today |
| Sentence context cards (PM-3) | Requires a sentence corpus; source good data first |
| HSK integration (PM-2) | Useful but secondary to core learning mechanics |
| Dark mode (UX-3) | Nice-to-have; lower impact than learning features |
| Local TTS (ENG-4) | Web Speech API works adequately for now |
| Card preview on hover (UX-5) | Minor convenience; low priority |

---

## Sources

- [Best Chinese Learning Apps 2025 (Migaku)](https://migaku.com/blog/chinese/best-chinese-learning-apps)
- [Top 10 Best Apps to Learn Chinese 2026 (LinguaSteps)](https://linguasteps.com/resources/top-10-best-apps-to-learn-chinese-in-2025)
- [17 Best Chinese Flashcard Apps 2026 (Joy of Chinese)](https://joyofchinese.com/chinese-flashcard/)
- [Anki Animated Stroke Order (Mandarin Mania)](https://mandarinmania.com/anki-animated-stroke-order/)
- [Make Me a Hanzi (GitHub)](https://github.com/skishore/makemeahanzi)
