import re
from validator.rules_src import Rule

_ATOM = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
_LABEL = r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"


class Mail(Rule):
    """
    The field under validation must be formatted as an e-mail address

    The local part may use the usual characters and single dots (64 characters at most), the domain has at least two
    labels and ends with an alphabetic top-level domain of two characters or more (254 characters at most in total).

    Examples:
    >>> from validator import validate

    >>> reqs = {"email_addr" : "abcd@ef.gh"}
    >>> rule = {"email_addr" : "mail"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"email_addr" : "first.last@mail.example.info"}
    >>> rule = {"email_addr" : "mail"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"email_addr" : "aaa.com"}
    >>> rule = {"email_addr" : "mail"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)
        self.regex = rf"(?P<local>{_ATOM}(?:\.{_ATOM})*)@(?:{_LABEL}\.)+[A-Za-z]{{2,63}}"

    def check(self, arg):
        if isinstance(arg, str) and len(arg) <= 254:
            match = re.fullmatch(self.regex, arg)
            if match is not None and len(match.group("local")) <= 64:
                return True

        self.set_error(f"Expected a Mail, Got: {arg}")
        return False

    def __from_str__(self):
        pass
