from validator.rules_src import Rule
from validator.rules_src.size import Size
from validator import utils


class In(Rule):
    """
    The in rule ensures that the value under validation exists within a predefined set of acceptable values.

    Examples:
    >>> from validator import validate

    >>> reqs = {"forge_version" : "latest"}
    >>> rule = {"forge_version" : "in:recommended,latest"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"forge_version" : "neoforge"}
    >>> rule = {"forge_version" : "in:recommended,latest"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, values: list):
        Rule.__init__(self)
        self.values = values

    def check(self, arg):
        if arg not in self.values:
            self.set_error(f"The selected argument is invalid.")
            return False

        return True

    def __from_str__(self):
        pass
