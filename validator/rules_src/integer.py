import re

from validator.rules_src import Rule

# An optional sign and ASCII digits; surrounding spaces are tolerated. Other bases have their own rules (Binary, Octal, Hex).
_BASE_10 = re.compile(r"\s*[+-]?[0-9]+\s*")


class Integer(Rule):
    """
    The field under validation must be a base-10 Integer (use Binary, Octal or Hex for other bases)

    Examples:
    >>> from validator import validate

    >>> reqs = {"num" : "23"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"num" : "value"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"num" : "0x1f"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
    False
    """

    aliases = ["int"]

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, int):
            return True

        if not isinstance(arg, str):
            self.set_error(f"Expected Type of Int or Str, Got: {type(arg)}")
            return False

        if _BASE_10.fullmatch(arg) is None:
            self.set_error(f"Expected String to be a base-10 integer, Got: {arg}")
            return False

        return True

    @staticmethod
    def convert(val):
        if isinstance(val, int):
            return val

        if isinstance(val, str) and _BASE_10.fullmatch(val) is not None:
            return int(val.strip(), 10)

        raise ValueError(f"Expected a base-10 integer, Got: {val}")

    def __from_str__(self):
        pass
