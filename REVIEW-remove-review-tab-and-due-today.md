# Code review: Remove Review tab and Due today logic

**Files reviewed:** 1 (`My Apps/chinese-flashcards/index.html`)

---

### Looks good

- **No console.log or debug** – Code is production-ready.
- **Backward compatibility** – Existing stats without `todayGoal` / `todayGoalDate` are safe: `(stats.todayGoal || 0)` and `stats.todayGoalDate === today` behave correctly when those fields are missing (e.g. after import or old localStorage).
- **Nav guard** – `showSection` only sets active on a nav button when one exists, so switching to `review` no longer throws.
- **Stats shape** – `todayGoal` and `todayGoalDate` are initialised in both default and catch blocks in `loadStats`, and cleared on day rollover.
- **Start Review unchanged** – Button still uses `dueCards.length` for label and disabled state; no unintended coupling to Due today.
- **Architecture** – Matches existing patterns (stats in localStorage, same cache/save flow, file sync unchanged).

---

### Issues found

- **HIGH** [index.html ~1491–1494] – Pre-filling the card limit on every `updateHomeStats` overwrites user input.
  - **What happens:** `#cardLimit` has an `input` listener that calls `updateHomeStats`. When `stats.todayGoalDate === today` and `stats.todayGoal > 0`, the code does `document.getElementById('cardLimit').value = stats.todayGoal`. So every keystroke (e.g. user changing 20 to 5) triggers `updateHomeStats` and the field is reset to `stats.todayGoal`, so the user cannot change the limit for the same day.
  - **Fix:** Only pre-fill when the field is empty or zero, so the persisted goal is restored when the user hasn’t entered a value yet, but we don’t overwrite while they’re typing:
  ```js
  if (stats.todayGoalDate === today && (stats.todayGoal || 0) > 0) {
      const el = document.getElementById('cardLimit');
      const val = el.value.trim();
      if (val === '' || parseInt(val, 10) === 0) el.value = stats.todayGoal;
  }
  ```

- **LOW** [index.html] – Edge case: if the user completes their daily goal (e.g. 20) and then starts another session the same day with a new limit (e.g. 10), we set `todayGoal = 10` but `todayReviewed` is already 20, so Due today becomes `max(0, 10 - 20) = 0`. The “remaining for today” display doesn’t reflect the second goal. Acceptable if the product is “one goal per day”; otherwise consider treating the goal as incremental or storing a “total goal for the day” and updating it when starting a new session (e.g. add to goal instead of replace).

---

### Summary

- **Files reviewed:** 1  
- **Critical issues:** 0  
- **Warnings (high):** 1 (card limit pre-fill overwriting input)  
- **Medium:** 0  
- **Low:** 1 (second-session same-day goal display)

Recommend applying the HIGH fix so users can change the card limit within the same day without the field reverting.
