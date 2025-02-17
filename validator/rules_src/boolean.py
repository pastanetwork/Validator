from validator.rules_src import Rule


class Boolean(Rule):
    """
    The field under validation must be a Boolean value.

    Examples:
    >>> from validator import validate

    >>> reqs = {"value" : True}
    >>> rule = {"value" : "boolean"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value" : "yes"}
    >>> rule = {"value" : "boolean"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value" : 17}
    >>> rule = {"value" : "boolean"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)
        self._boolean_values = {True, 'true', '1', 1, 'on', 'yes', False, 'false', '0', 0, 'off', 'no'}

    def check(self, arg):
        if arg in self._boolean_values:
            return True
        return False

    def __from_str__(self):
        pass
