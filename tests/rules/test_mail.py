from validator.rules import Mail
from validator import validate


def test_mail_01():
    assert Mail().check("sdar@quecompde.ga")

    assert Mail().check("awavufo@yopmail.com")

    assert Mail().check("nawuteny@gmail.com")

    assert Mail().check("rapattullatta@yandex.ru")


def test_mail_02():
    assert not Mail().check("sdar@quecompde")

    assert not Mail().check("@yopmail.com")

    assert not Mail().check("nawuteny-6603@com")

    assert not Mail().check("rapattullatta-2328@z")


def test_mail_03_string():
    assert validate({"val": "sdar@quecompde.ga"}, {"val": "mail"})

    assert validate({"val": "peter@griffin.com"}, {"val": "mail"})

    assert not validate({"val": "jeje.ge"}, {"val": "mail"})

    assert not validate({"val": "name@com"}, {"val": "mail"})


def test_mail_04_common_addresses():
    assert Mail().check("a@example.com")

    assert Mail().check("First.Last@Example.COM")

    assert Mail().check("x@mail.example.co.uk")

    assert Mail().check("team+news@example.info")

    assert Mail().check("o'neil_2@sub-domain.example.org")


def test_mail_05_malformed_addresses():
    assert not Mail().check("a..b@example.com")

    assert not Mail().check(".a@example.com")

    assert not Mail().check("a.@example.com")

    assert not Mail().check("a@-example.com")

    assert not Mail().check("a@example..com")

    assert not Mail().check("a@example.c")

    assert not Mail().check("a@example.123")

    assert not Mail().check("a b@example.com")

    assert not Mail().check("a@example.com ")

    assert not Mail().check("a@b@example.com")


def test_mail_06_lengths():
    assert Mail().check("a" * 64 + "@example.com")

    assert not Mail().check("a" * 65 + "@example.com")

    assert not Mail().check("a@" + "b" * 63 + "." + "c" * 63 + "." + "d" * 63 + "." + "e" * 63 + ".com")

    assert not Mail().check(12)
