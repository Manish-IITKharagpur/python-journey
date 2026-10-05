"""
Sum of two lowest positive integers (7 kyu)
https://www.codewars.com/kata/558fc85d8fd1938afb000014

Return the sum of the two lowest numbers in a list of at least 4
positive integers. No floats or non-positive integers will be passed.

Examples:
    [19, 5, 42, 2, 77]                       => 7      (2 + 5)
    [10, 343445353, 3453445, 3453545353453]  => 3453455 (10 + 3453445)
"""


def sum_two_smallest_numbers(numbers):
    result = sorted(numbers)
    return result[0]+result[1]
    


if __name__ == "__main__":
    tests = [
        ([19, 5, 42, 2, 77], 7),
        ([10, 343445353, 3453445, 3453545353453], 3453455),
        ([5, 8, 12, 18, 22], 13),        # already sorted
        ([22, 18, 12, 8, 5], 13),        # sorted backwards
        ([3, 3, 10, 20], 6),             # the smallest number appears twice
        ([7, 15, 12, 18, 22], 19),       # smallest two are not next to each other
    ]
    for numbers, expected in tests:
        original = list(numbers)         # keep a copy to check the input isn't changed
        try:
            got = sum_two_smallest_numbers(numbers)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        ok = got == expected and numbers == original
        note = "" if numbers == original else f"  (input list was changed to {numbers})"
        print(f"{'PASS' if ok else 'FAIL'}  sum_two_smallest_numbers({original!r}) -> {got!r}, expected {expected!r}{note}")
