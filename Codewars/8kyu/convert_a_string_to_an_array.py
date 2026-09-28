"""
Convert a string to an array (8 kyu)
https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

Write a function that splits a string of space-separated words into a
list of words. Words are separated by exactly one space, and there are no
leading or trailing spaces. A "word" is any run of characters without a space.

Examples:
    "string"                             => ["string"]
    "Robin Singh"                        => ["Robin", "Singh"]
    "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""


def string_to_array(s):
    # your code here
    return s.split(" ")


if __name__ == "__main__":
    tests = [
        ("string", ["string"]),
        ("Robin Singh", ["Robin", "Singh"]),
        ("I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]),
        ("hello, world!", ["hello,", "world!"]),   # punctuation stays part of the word
        ("a1 b2 c3", ["a1", "b2", "c3"]),          # digits are part of words too
    ]
    for s, expected in tests:
        got = string_to_array(s)
        print(f"{'PASS' if got == expected else 'FAIL'}  string_to_array({s!r}) -> {got!r}, expected {expected!r}")
