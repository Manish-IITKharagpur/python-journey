# Codewars

Daily Python practice with [Codewars](https://www.codewars.com) katas.

Each kata lives in `<rank>kyu/<name>.py` with its description and test cases. From this folder, run one with:

```bash
python 6kyu/valid_braces.py
```

## Progress

| Date | Kata | Rank | Solution | Key idea |
|---|---|---|---|---|
| 2026-09-13 | [Flick Switch](https://www.codewars.com/kata/64fbfe2618692c2018ebbddb) | 8 kyu | [flick_switch.py](8kyu/flick_switch.py) | Toggle a boolean with `state = not state` |
| 2026-09-13 | [Convert a string to an array](https://www.codewars.com/kata/57e76bc428d6fbc2d500036d) | 8 kyu | [convert_a_string_to_an_array.py](8kyu/convert_a_string_to_an_array.py) | `s.split()` splits a string into a list of words |
| 2026-09-28 | [Valid Braces](https://www.codewars.com/kata/5277c8a221e209d3f6000b56) | 6 kyu | [valid_braces.py](6kyu/valid_braces.py) | Stack: last opened must be first closed; empty stack at the end = valid |
| 2026-09-28 | [Sum of positive](https://www.codewars.com/kata/5715eaedb436cf5606000381) | 8 kyu | [sum_of_positive.py](8kyu/sum_of_positive.py) | Loop with a running total; never name a variable `sum` (it hides the built-in) |
| 2026-10-02 | [Counting sheep...](https://www.codewars.com/kata/54edbc7200b811e956000556) | 8 kyu | [counting_sheep.py](8kyu/counting_sheep.py) | `list.count(True)` counts matches; `is True` vs `== True` (1 == True); `sum()` crashes on None |
| 2026-10-02 | [Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3) | 7 kyu | [vowel_count.py](7kyu/vowel_count.py) | Loop over a string char by char; `ch in "aeiou"` replaces a chain of `or` checks |
| 2026-10-02 | [Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e) | 7 kyu | [disemvowel_trolls.py](7kyu/disemvowel_trolls.py) | Build a new string with `result += ch`; `ch.lower()` handles both cases; `x not in a or b` is a trap (a bare string is always truthy) |
| 2026-10-05 | [Jaden Casing Strings](https://www.codewars.com/kata/5390bac347d09b7da40006f6) | 7 kyu | [jaden_casing_strings.py](7kyu/jaden_casing_strings.py) | Split, change, join; `word[0].upper() + word[1:]`; `.title()` breaks contractions (Aren'T) |
