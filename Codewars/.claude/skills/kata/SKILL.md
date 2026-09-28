---
name: kata
description: Daily Codewars practice workflow. Use when Manish names a kata to solve ("today I'm solving 6kyu valid braces"), asks for a new kata ("give me an 8 kyu on strings"), asks for a hint or review on a kata, or says a kata is done and should be committed.
---

# Daily kata workflow

Follow CLAUDE.md's tutoring rules throughout: hints before answers, code only when asked.

## 1. Set up the kata

1. Find the kata. If given a name, turn it into a slug (`valid braces` -> `valid-braces`) and fetch:
   ```bash
   curl -s https://www.codewars.com/api/v1/code-challenges/<slug> | python -c "import sys,json;d=json.load(sys.stdin);print(d['name'],d['rank']['name'],d['url']);print(d['description'])"
   ```
   If the slug 404s, search the web for the kata's Codewars URL and use its id. If asked for a random kata at a level/topic, suggest 2-3 real katas you know and let Manish pick.
2. Create `<rank>kyu/<slug_with_underscores>.py` (e.g. `6kyu/valid_braces.py`). Don't overwrite an existing file — if it exists, Manish is resuming; read it instead.
3. File contents:
   - Docstring: name, rank, URL, description rewritten in plain text (strip Codewars `~~~if:` language blocks and non-Python parts), examples.
   - Function stub with `# Write your solution here` and `pass`. Use the function name Codewars uses for Python.
   - `if __name__ == "__main__":` block with a list of `(input, expected)` tests that prints `PASS`/`FAIL` per case. Include the kata's examples plus edge cases, each extra case with a short comment on what it catches.
4. Run the file once to confirm it executes (stub tests will FAIL, that's expected).
5. Tell Manish the file path, the run command, and give a 3-level hint ladder in collapsible `<details>` blocks (Hint 1 = the key insight, Hint 2 = data structure/technique, Hint 3 = near-implementation detail).

## 2. While solving

- If Manish describes an approach: confirm what's right, correct what's off with a concrete counter-example input, point out edge cases they missed.
- If a test fails: read their code and the failing output, explain *why* with a trace table, but let them fix it.
- Only write the solution when explicitly asked ("show me the code"). Then put it in the file, run the tests, and explain each line.

## 3. After it passes

1. Run the file and confirm every test PASSes.
2. Review: correctness, edge cases, readability, and a more Pythonic alternative if one exists (show it, don't replace their code unless asked).
3. Add a row to the README progress table: date (YYYY-MM-DD), kata name linked to its URL, rank, file link, one-line "key idea" (e.g. "stack: last opened, first closed").
4. Commit and push:
   ```bash
   git add -A && git commit -m "Solve <Kata Name> (<rank> kyu)" && git push
   ```
5. Suggest a next kata that builds on the same idea.
