import re
from validator.rules_src import Rule


class Url(Rule):
    """
    The field under validation must be a valid URL

    Examples:
    >>> from validator import validate

    >>> reqs = {"website" : "https://www.example.com"}
    >>> rule = {"website" : "url"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"website" : "http://example.com/path?query=value"}
    >>> rule = {"website" : "url"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"website" : "not a url"}
    >>> rule = {"website" : "url"}
    >>> validate(reqs, rule)
    False
    """

    aliases = ["url"]

    def __init__(self):
        Rule.__init__(self)
        # Regex pattern for URL validation
        # Supports http, https, ftp protocols and optional www
        self.regex = r"^(https?|ftp):\/\/" \
                     r"(([a-zA-Z0-9\-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9\-_]+\.[a-zA-Z]{2,}|" \
                     r"localhost|" \
                     r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" \
                     r"(:\d+)?" \
                     r"(\/[^\s]*)?$"

    def check(self, arg):
        if not isinstance(arg, str):
            self.set_error(f"Expected a String, Got: {type(arg).__name__}")
            return False

        if re.match(self.regex, arg) is not None:
            return True

        self.set_error(f"Expected a valid URL, Got: {arg}")
        return False

    def __from_str__(self):
        pass
