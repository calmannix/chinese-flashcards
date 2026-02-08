# Chinese Vocabulary Flashcards

Browser-based spaced repetition app for memorising Traditional Chinese vocabulary.

## Quick start

```bash
open index.html
```

Or drag `index.html` into Chrome.

## What it does

- Stores vocabulary: pinyin, Traditional characters, English translation
- Four activity modes: Memorise, Translate ZH/EN, Translate EN/ZH, Complete Learning
- Schedules reviews using the SM-2 algorithm (same as Anki)
- Smart Shuffle filter prioritises difficult words (60% hard, 25% good, 15% easy)
- Filters reviews by lesson and card limit
- Tracks daily streak and session stats
- Colours pinyin by tone (red/orange/green/blue for tones 1-4)
- Pinyin-to-character lookup from a built-in ~11,000 word dictionary
- Optional file sync (Chrome/Edge) for persistent backup

## Adding vocabulary

1. Click **Add Words**
2. In the **Traditional Characters** field, type pinyin (e.g. `xuesheng`)
3. A dropdown appears with matching words from the dictionary
4. Click a result to fill the characters, pinyin, and English fields
5. Optionally assign a **Lesson** (e.g. "Lesson 1"). The lesson persists for the next word you add.
6. Click **Add Word**

**Alternative**: Enter characters directly if you have a Chinese keyboard, or if the word isn't in the dictionary.

**Pinyin input formats**:
- Tone numbers: `xue2sheng1` or `xue2 sheng1`
- Without tones: `xuesheng` (shows all tone variants)

Each word creates two flashcards: one Chinese-to-English, one English-to-Chinese.

## Reviewing

### Starting a session

On the home screen:

1. **Study from** dropdown:
   - **Smart Shuffle**: Focuses on difficult words. Requires a session size. Selects 60% hard cards, 25% good, 15% easy.
   - **All Words**: Reviews entire vocabulary
   - **Lesson name**: Reviews only cards from that lesson
2. **Session size**: Limit number of cards (optional for All Words and Lesson filters, required for Smart Shuffle)
3. **Activity mode**:
   - **Memorise**: Shows characters, pinyin, and English together. Grade buttons appear immediately. Grading applies to both direction cards for the word.
   - **ZH / EN**: Shows the English translation. You recall the Chinese. Reveal shows characters and pinyin.
   - **EN / ZH**: Shows characters and pinyin. You recall the English. Reveal shows the translation.
   - **Complete**: Three-phase learning. Phase 1: Memorise (4-button grading). Phases 2 and 3: Test recall in both directions (binary Correct/Incorrect). Incorrect cards re-queue until all are correct.
4. Click **Start Review**

### Grading

**Memorise mode and Complete Learning Phase 1:**

- **Again**: Re-queue the card. When you eventually grade it Hard/Good/Easy, the card is forced to Hard and its interval resets to 1 day.
- **Hard**: Got lucky. Needs more repetition. Shorter interval.
- **Good**: Correct but not fully confident. Standard interval.
- **Easy**: Know it already. Longer interval, shown less often.

**ZH/EN, EN/ZH modes and Complete Learning Phases 2-3:**

- **Incorrect**: Re-queue the card. Try again in this session. Forced to Good grade when correct.
- **Correct**: Standard interval. Move to next card.

## Data storage

All data lives in your browser's localStorage. No server, no account, no internet required.

**Important**: Clearing browser data deletes your vocabulary. Export regularly or use file sync.

### File sync (Chrome/Edge)

1. Go to **Add Words**
2. Click **Link Storage File** and choose a `.json` file
3. Data auto-syncs to that file on every change
4. On next visit, the app restores from the linked file

### Export and import

1. Go to **Add Words**
2. Click **Export JSON** to download your vocabulary
3. To restore: click **Import JSON** and select the file

## Tone colours

| Tone | Colour | Example |
|------|--------|---------|
| 1 (flat) | Red | ma |
| 2 (rising) | Orange | ma |
| 3 (dip) | Green | ma |
| 4 (falling) | Blue | ma |
| 5 (neutral) | Grey | ma |

## Technical details

- Single HTML file + dictionary.js (~7MB)
- Vanilla JavaScript, no framework
- Works offline once loaded
- Dictionary: ~11,000 entries from CC-CEDICT (CC BY-SA 4.0)

## SM-2 algorithm

The app uses a modified SuperMemo 2 algorithm:

- New cards start with a 1-day interval
- Successful reviews increase the interval by the ease factor (~2.5x)
- **Again/Incorrect** re-queues the card in the current session. When eventually graded Hard/Good/Easy (or Correct), forces a Hard grade with repetitions reset to 0 (restarts at 1-day interval)
- **Hard** applies a 0.8x interval multiplier
- **Good/Correct** uses standard SM-2 progression
- **Easy** applies a 1.3x interval multiplier
- Ease factor adjusts per card based on your history (minimum 1.3)
- In Memorise mode and Complete Learning Phase 1, grading a card also grades its sibling (opposite direction) to keep scheduling in sync
- Complete Learning Phases 2-3 use binary Correct/Incorrect, mapped to Good/Again internally
