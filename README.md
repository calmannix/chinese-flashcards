# Riri (日日)

Spaced repetition flashcard app for learning Traditional Chinese. Runs offline on macOS.

![Python](https://img.shields.io/badge/Python_3-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/Vanilla_JS-F7DF1E?logo=javascript&logoColor=black)
![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white)

## What it does

- SM-2 spaced repetition: difficult words appear more often, easy words fade back
- Radical decomposition: breaks characters into components with English meanings
- Progress dashboard: streak counter, 90-day heatmap, accuracy trends, mastery distribution
- Keyboard-first review: Space to flip, 1-4 to grade
- Built-in dictionary with pinyin suggestions when adding words
- Multiple study modes for words (Memorise, ZH/EN, EN/ZH, Complete) and phrases (Memorise, Translate, Reading, Complete)

## Getting started

1. Download or clone this repo
2. Double-click **Chinese Flashcards.app**
3. The app starts a local server and opens in your browser

Requires Python 3 on your Mac. No internet needed after first launch.

## How it works

The .app bundle wraps a Python HTTP server (localhost:8080) serving a single-page vanilla JS frontend. Your vocabulary and progress save to ~/Library/Application Support/Chinese Flashcards/data.json. Nothing leaves your machine.

## Keyboard shortcuts

| Key | Action |
|-----|--------|
| Space | Flip the card |
| 1 | Again |
| 2 | Hard |
| 3 | Good |
| 4 | Easy |

## Pinyin tone colours

- Red = 1st tone (flat)
- Orange = 2nd tone (rising)
- Green = 3rd tone (dip)
- Blue = 4th tone (falling)
- Grey = neutral tone

## Built with

- Vanilla JavaScript, HTML, CSS (no frameworks)
- Python 3 HTTP server
- SM-2 spaced repetition algorithm
- Radical data from [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) (9,490 characters)
- Built with [Claude Code](https://claude.ai/claude-code)
