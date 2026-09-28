"""
Valid Braces (6 kyu)
https://www.codewars.com/kata/5277c8a221e209d3f6000b56

Write a function that takes a string of braces and determines if the order
of the braces is valid. Return True if valid, False otherwise.

Input is non-empty and only contains: ()[]{}
A string is valid if every brace is matched with the correct brace.

Examples:
    "(){}[]"   => True
    "([{}])"   => True
    "(}"       => False
    "[(])"     => False
    "[({})](]" => False
"""


def valid_braces(string):
    pairs = {')': '(', ']': '[', '}': '{'}  # closing -> matching opening
    stack = []

    for char in string:
        if char in '([{':
            stack.append(char)
        else:
            # closing bracket with nothing open, or the wrong one open
            if not stack or stack.pop() != pairs[char]:
                return False

    # anything left over was opened but never closed
    return not stack


if __name__ == "__main__":
    tests = [
        ("(){}[]", True),
        ("([{}])", True),
        ("(}", False),
        ("[(])", False),
        ("[({})](]", False),
        ("(", False),          # never closed
        (")", False),          # closes before opening
        ("())(", False),       # counts match but order is wrong
        ("{[()()]}[]", True),
    ]
    for s, expected in tests:
        got = valid_braces(s)
        print(f"{'PASS' if got == expected else 'FAIL'}  valid_braces({s!r}) -> {got!r}, expected {expected!r}")
