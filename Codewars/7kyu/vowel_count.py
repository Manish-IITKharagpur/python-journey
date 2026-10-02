"""
Vowel Count (7 kyu)
https://www.codewars.com/kata/54ff3102c1bad923760001f3

Return the number (count) of vowels in the given string.

Vowels for this kata are a, e, i, o, u (not y).
The input string only contains lowercase letters and/or spaces.

Example:
    "abracadabra" => 5
"""


def get_count(sentence):
    count = 0
    for ch in sentence:
        if ch in "aeiou":
            count += 1
    return count


if __name__ == "__main__":
    tests = [
        ("abracadabra", 5),
        ("aeiou", 5),               # only vowels
        ("bcdfg", 0),               # no vowels at all
        ("", 0),                    # empty string
        ("y", 0),                   # y is NOT a vowel here
        ("my pyx", 0),              # spaces and y's, still no vowels
        ("hello world", 3),         # spaces are not vowels
        ("o a kak ushakov lil vo kashu kakao", 13),
    ]
    for s, expected in tests:
        try:
            got = get_count(s)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        print(f"{'PASS' if got == expected else 'FAIL'}  get_count({s!r}) -> {got!r}, expected {expected!r}")
