"""
Counting sheep... (8 kyu)
https://www.codewars.com/kata/54edbc7200b811e956000556

You get a list of sheep where some sheep may be missing from their place.
Count the number of sheep present in the list (True means present).

Watch out for bad values like None: they are not sheep.

Example:
    [True,  True,  True,  False,
     True,  True,  True,  True,
     True,  False, True,  False,
     True,  False, False, True,
     True,  True,  True,  True,
     False, False, True,  True]   => 17
"""
def count_sheeps(sheep):
    return sheep.count(True)

if __name__ == "__main__":
    tests = [
        ([True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True], 17),
        ([], 0),                            # empty field
        ([False, False], 0),                # all sheep missing
        ([True, True, True], 3),            # all sheep present
        ([True, None, False, True], 2),     # None is a bad value, not a sheep
        ([None, None], 0),                  # only bad values
    ]
    for sheep, expected in tests:
        try:
            got = count_sheeps(sheep)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        print(f"{'PASS' if got == expected else 'FAIL'}  count_sheeps({sheep!r}) -> {got!r}, expected {expected!r}")
