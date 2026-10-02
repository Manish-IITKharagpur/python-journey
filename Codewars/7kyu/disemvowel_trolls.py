"""
Disemvowel Trolls (7 kyu)
https://www.codewars.com/kata/52fba66badcd10859f00097e

Trolls are attacking your comment section! Neutralize them by removing all
the vowels from their comments.

Write a function that takes a string and returns a new string with all
vowels removed. For this kata, y is not a vowel.

Example:
    "This website is for losers LOL!" => "Ths wbst s fr lsrs LL!"
"""


def disemvowel(string_):
    result =""
    for ch in string_:
        if ch.lower() not in 'aeiou':
            result= result + ch
        
    return result
if __name__ == "__main__":
    tests = [
        ("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
        ("AEIOU aeiou", " "),                    # UPPERCASE vowels count too
        ("No offense but,\nYour writing is among the worst I've ever read",
         "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
        ("What are you, a communist?", "Wht r y,  cmmnst?"),  # "a" alone leaves two spaces
        ("rhythm", "rhythm"),                    # y is NOT a vowel, nothing removed
        ("", ""),                                # empty string
    ]
    for s, expected in tests:
        try:
            got = disemvowel(s)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        print(f"{'PASS' if got == expected else 'FAIL'}  disemvowel({s!r}) -> {got!r}, expected {expected!r}")
