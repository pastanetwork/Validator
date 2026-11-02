from validator.rules_src import Rule
import re
from re import compile

# Flags accepted after a delimited pattern, such as "/^foo$/i".
_DELIMITED = re.compile(r"^/(.*)/([imsxu]*)$", re.DOTALL)
_FLAGS = {"i": re.IGNORECASE, "m": re.MULTILINE, "s": re.DOTALL, "x": re.VERBOSE, "u": 0}


class Regex(Rule):
    """
    The field under validation must match the given regular expression.

    Examples:
    >>> from validator import validate

    >>> reqs = {"value" : "PythonValidator"}
    >>> rule = {"value" : "regex:^[0-9a-zA-Z]*$"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value" : "Python_Validator"}
    >>> rule = {"value" : "regex:^[0-9a-zA-Z]*$"}
    >>> validate(reqs, rule)
    False

    The pattern may be delimited by slashes, with optional flags (i, m, s, x, u), as in Laravel rules:

    >>> reqs = {"value" : "PythonValidator"}
    >>> rule = {"value" : "regex:/^pythonvalidator$/i"}
    >>> validate(reqs, rule)
    True
    """

    def __init__(self, pattern):
        Rule.__init__(self)
        delimited = _DELIMITED.match(pattern)
        flags = 0
        if delimited:
            pattern = delimited.group(1)
            for flag in delimited.group(2):
                flags |= _FLAGS[flag]
        self.pattern = compile(pattern, flags)

    def check(self, arg):
        if not isinstance(arg, str):
            self.set_error(f"Expected a String, Got: {type(arg).__name__}")
            return False

        if self.pattern.search(arg):
            return True

        self.set_error(f"Expected to follow regex {self.pattern.pattern}, Got: {arg}")
        return False

    def __from_str__(self):
        pass
