import re
from validator.rules_src import Rule


class AlphaDash(Rule):
    """
    The field under validation may only contain letters, numbers, dashes, and underscores.

    Examples:
    >>> from validator import validate

    >>> reqs = {"username" : "user_name-123"}
    >>> rule = {"username" : "alpha_dash"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"username" : "user@name"}
    >>> rule = {"username" : "alpha_dash"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"username" : "username!"}
    >>> rule = {"username" : "alpha_dash"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)
        self._regex = r"^[a-zA-Z0-9-_]+$"

    def check(self, arg):
        return bool(re.match(self._regex, arg))

    def __from_str__(self):
        pass
