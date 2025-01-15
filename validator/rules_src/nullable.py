from validator.rules_src import Rule


class Nullable(Rule):
    """
    The field under validation must be present in the input data and not empty,
    unless it is explicitly set to None (nullable).

    Examples:
    >>> from validator import validate

    >>> reqs = {"value": "Not Empty"}
    >>> rule = {"value": "nullable_required"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value": ""}
    >>> rule = {"value": "nullable_required"}
    >>> validate(reqs, rule)
    False

    >>> reqs = {"value": None}
    >>> rule = {"value": "nullable_required"}
    >>> validate(reqs, rule)
    True
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if arg is None:
            return True

        # Check for empty values
        if hasattr(arg, "__len__") and len(arg) == 0:
            self.set_error("Field was empty")
            return False

        return True

    def __from_str__(self):
        pass
