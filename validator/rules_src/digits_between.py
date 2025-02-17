from validator.rules_src.digits import Digits
from validator.rules_src.max import Max
from validator.rules_src.min import Min


class DigitsBetween(Min, Max):
    """
    The field under validation must contain only numeric digits, and its length must be between the given min and max digits.

    Examples:
    >>> from validator import validate

    >>> reqs = {"phone_number" : "9876543210"}
    >>> rule = {"phone_number" : "digits_between:10,15"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"phone_number" : "12345abc"}
    >>> rule = {"phone_number" : "digits_between:10,15"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"phone_number" : "1234567890"}
    >>> rule = {"phone_number" : "digits_between:10,15"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"phone_number" : "123456789012345"}
    >>> rule = {"phone_number" : "digits_between:10,15"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"phone_number" : "123456789"}
    >>> rule = {"phone_number" : "digits_between:10,15"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, min_value, max_value):
        Min.__init__(self, min_value)
        Max.__init__(self, max_value)

    def check(self, arg):
        if not Digits().check(arg):
            return False
        if Min.check(self, arg) and Max.check(self, arg):
            return True
        return False

    def __from_str__(self):
        Min.__from_str__(self)
        Max.__from_str__(self)

