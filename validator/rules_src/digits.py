from validator.rules_src import Rule


class Digits(Rule):
    """
    The field under validation must be composed solely of digits.

    Given value is evaluated to check if it contains only numeric digits,
    and it can be a string or an integer. If the value is negative,
    the negative sign is ignored for validation.

    Examples:
    >>> from validator import validate

    >>> reqs = {"phone_number" : "1234567890"}
    >>> rule = {"phone_number" : "digits"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"phone_number" : "-9876543210"}
    >>> rule = {"phone_number" : "digits"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"phone_number" : "12345abc"}
    >>> rule = {"phone_number" : "digits"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"phone_number" : "1234.56"}
    >>> rule = {"phone_number" : "digits"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            value_str = str(arg)
            if value_str.startswith('-'):
                value_str = value_str[1:]
            return value_str.isdigit()
        except:
            pass
        return False

    def __from_str__(self):
        pass
