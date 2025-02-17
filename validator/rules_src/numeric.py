import math

from validator.rules_src import Rule


class Numeric(Rule):
    """
    The field under validation must be a numeric value, which can be either an integer or a floating-point number.

    Examples:
    >>> from validator import validate

    >>> reqs = {"num" : "23"}
    >>> rule = {"num" : "numeric"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"num" : "10.5"}
    >>> rule = {"num" : "numeric"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"num" : "value"}
    >>> rule = {"num" : "numeric"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"num" : "-5.3"}
    >>> rule = {"num" : "numeric"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"num" : "-5"}
    >>> rule = {"num" : "numeric"}
    >>> validate(reqs, rule)
    True
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, int) or isinstance(arg, float):
            return True

        if not isinstance(arg, str):
            self.set_error(f"Expected Type of Int or Str, Got: {type(arg)}")
            return False

        try:
            _ = float(arg)
            return not math.isnan(_)
        except ValueError:
            self.set_error(f"Expected String to be in Binary format, Got: {arg}")
            return False

    def __from_str__(self):
        pass
