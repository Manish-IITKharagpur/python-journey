"""
Jaden Casing Strings (7 kyu)
https://www.codewars.com/kata/5390bac347d09b7da40006f6

Jaden Smith is known for capitalizing every word when he writes on Twitter.
Convert a string so the first letter of every word is uppercase.
Watch how contractions are expected to look in the example.

Example:
    Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
    Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""


def to_jaden_case(string):
    words = string.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:] )
    
    return " ".join(result)

if __name__ == "__main__":
    tests = [
        ("How can mirrors be real if our eyes aren't real",
         "How Can Mirrors Be Real If Our Eyes Aren't Real"),
        ("aren't", "Aren't"),                    # contraction: the t after ' stays lowercase
        ("i'm don't you're", "I'm Don't You're"),  # several contractions
        ("school is the tool to brainwash the youth",
         "School Is The Tool To Brainwash The Youth"),
        ("hello", "Hello"),                      # a single word
    ]
    for s, expected in tests:
        try:
            got = to_jaden_case(s)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        print(f"{'PASS' if got == expected else 'FAIL'}  to_jaden_case({s!r}) -> {got!r}, expected {expected!r}")
