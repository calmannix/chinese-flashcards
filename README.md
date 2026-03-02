# 🀄 chinese-flashcards

Browser-based spaced repetition for Traditional Chinese vocabulary. No app, no account, no server — open `index.html` and study.

Built to learn Mandarin while living in Taipei. I wanted something as solid as Anki but with zero setup friction.

---

## Quick start

```bash
open index.html
```

Or drag `index.html` into Chrome.

---

## Features

- **Four study modes**: Memorise, ZH→EN, EN→ZH, Complete Learning
- **SM-2 algorithm**: Same spaced repetition as Anki — cards you struggle with come back sooner
- **Smart Shuffle**: Prioritises hard cards (60% hard, 25% good, 15% easy)
- **Tone colours**: Pinyin coloured by tone (red/orange/green/blue)
- **11,000-word dictionary**: Type pinyin, pick from a dropdown, characters fill automatically
- **Lesson filtering**: Organise vocab by lesson or topic
- **Streak tracking**: Daily study streak and session stats
- **File sync**: Optional persistent backup via Chrome/Edge file API

---

## Adding words

1. Click **Add Words**
2. Type pinyin in the Traditional Characters field (e.g. `xuesheng`)
3. Pick a match from the dropdown — characters, pinyin, and English fill in
4. Assign a lesson if you want (it carries over to the next word)
5. Click **Add Word**

Each word creates two cards: Chinese→English and English→Chinese.

---

## Data

Everything lives in `localStorage`. No internet required once loaded.

Export regularly: **Add Words → Export JSON**. To restore: **Import JSON**.

**File sync (Chrome/Edge):** Link a `.json` file under Add Words and the app syncs automatically on every change.

---

## Stack

Vanilla JavaScript · Single HTML file · CC-CEDICT dictionary (CC BY-SA 4.0)
