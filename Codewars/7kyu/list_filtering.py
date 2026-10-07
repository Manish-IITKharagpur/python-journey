"""
List Filtering (7 kyu)
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

Take a list of non-negative integers and strings, and return a NEW list
with the strings filtered out.

Examples:
    [1, 2, 'a', 'b']                  => [1, 2]
    [1, 'a', 'b', 0, 15]              => [1, 0, 15]
    [1, 2, 'aasf', '1', '123', 123]   => [1, 2, 123]
"""


def filter_list(l):
    return [item for item in l if not isinstance(item, str)]


if __name__ == "__main__":
    tests = [
        ([1, 2, 'a', 'b'], [1, 2]),
        ([1, 'a', 'b', 0, 15], [1, 0, 15]),
        ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123]),
        (['a', 'b', 'c'], []),            # only strings: nothing left
        ([], []),                         # empty list
        ([0, 0], [0, 0]),                 # 0 is a number and must be kept
        (['0', 0, '7', 7], [0, 7]),       # '7' looks like a number but is a string
        ([3, 'x', 1, 'y', 2], [3, 1, 2]), # keep the original order
    ]
    for l, expected in tests:
        original = list(l)                # keep a copy to check the input isn't changed
        try:
            got = filter_list(l)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        ok = got == expected and l == original
        note = "" if l == original else f"  (input list was changed to {l})"
        print(f"{'PASS' if ok else 'FAIL'}  filter_list({original!r}) -> {got!r}, expected {expected!r}{note}")
