"""
Flick Switch (8 kyu)
https://www.codewars.com/kata/64fbfe2618692c2018ebbddb

Create a function that returns True for every item in a given list.
However, if an element is the word 'flick', switch to returning the
opposite boolean value.

Notes:
    - "flick" is always lowercase.
    - A list may contain multiple flicks.
    - The switch happens on the same element as the flick itself.

Examples:
    ['codewars', 'flick', 'code', 'wars']            => [True, False, False, False]
    ['flick', 'chocolate', 'adventure', 'sunshine']  => [False, False, False, False]
    ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] => [True, True, False, False, True]
"""


def flick_switch(lst):
    state = True
    results = []

    for word in lst:
        if word == "flick":
          state = not state
        results.append(state)
    return results


if __name__ == "__main__":
    tests = [
        (['codewars', 'flick', 'code', 'wars'], [True, False, False, False]),
        (['flick', 'chocolate', 'adventure', 'sunshine'], [False, False, False, False]),
        (['bicycle', 'jarmony', 'flick', 'sheep', 'flick'], [True, True, False, False, True]),
        ([], []),                                   # empty list
        (['flick', 'flick'], [False, True]),        # back-to-back flicks switch twice
        (['a', 'b', 'c'], [True, True, True]),      # no flick at all
        (['flickering', 'flick'], [True, False]),   # only the exact word 'flick' counts
    ]
    for lst, expected in tests:
        got = flick_switch(lst)
        print(f"{'PASS' if got == expected else 'FAIL'}  flick_switch({lst!r}) -> {got!r}, expected {expected!r}")
