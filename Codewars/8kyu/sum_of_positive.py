"""
Sum of positive (8 kyu)
https://www.codewars.com/kata/5715eaedb436cf5606000381

You get a list of numbers. Return the sum of all the positive ones.
If there is nothing to sum, the sum defaults to 0.

Example:
    [1, -4, 7, 12] => 1 + 7 + 12 = 20
"""


def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    
    return total


if __name__ == "__main__":
    tests = [
        ([1, -4, 7, 12], 20),
        ([1, 2, 3, 4, 5], 15),      # all positive
        ([-1, -2, -3], 0),          # all negative: nothing to sum
        ([], 0),                    # empty list
        ([0, 0, 5], 5),             # 0 is not positive, but adding it changes nothing
        ([-5, 10], 10),             # negative first
    ]
    for arr, expected in tests:
        got = positive_sum(arr)
        print(f"{'PASS' if got == expected else 'FAIL'}  positive_sum({arr!r}) -> {got!r}, expected {expected!r}")
