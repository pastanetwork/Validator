import re
from validator.rules_src import Rule


class AlphaNum(Rule):
    """
    The field under validation must contain only letters and numbers.

    Examples:
    >>> from validator import validate

    >>> reqs = {"username" : "user123"}
    >>> rule = {"username" : "alpha_num"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"username" : "user_name"}
    >>> rule = {"username" : "alpha_num"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"username" : "12345"}
    >>> rule = {"username" : "alpha_num"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"username" : "user@name"}
    >>> rule = {"username" : "alpha_num"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)
        self._regex = r"^[a-zA-Z0-9]+$"

    def check(self, arg):
        return bool(re.match(self._regex, arg))

    def __from_str__(self):
        pass
