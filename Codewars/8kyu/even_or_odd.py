"""
Even or Odd (8 kyu)
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

Create a function that takes an integer as an argument and returns
"Even" for even numbers or "Odd" for odd numbers.
"""


def even_or_odd(number):
    # Write your solution here
    pass


if __name__ == "__main__":
    tests = [(2, "Even"), (1, "Odd"), (0, "Even"), (7, "Odd"), (-42, "Even"), (-7, "Odd")]
    for n, expected in tests:
        got = even_or_odd(n)
        print(f"{'PASS' if got == expected else 'FAIL'}  even_or_odd({n}) -> {got!r}, expected {expected!r}")
