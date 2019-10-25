from fraction import Fraction


def assert_equals(expect, actual):
    if expect != actual:
        message = "expect: " + str(expect) + ", but actual: " + str(actual)
        raise Exception(message)


f1 = Fraction(2, 3)
f2 = Fraction(3, 4)

assert_equals(Fraction(17, 12), f1 + f2)
assert_equals(Fraction(-1, 12), f1 - f2)
assert_equals(Fraction(1, 2), f1 * f2)
assert_equals(Fraction(8, 9), f1 / f2)
assert_equals(False, f1 == f2)
assert_equals(True, f1 != f2)
assert_equals(True, f1 < f2)
assert_equals(True, f1 <= f2)
assert_equals(False, f1 > f2)
assert_equals(False, f1 >= f2)