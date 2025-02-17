from validator.rules import Digits
from validator.rule_pipe_validator import RulePipeValidator as RPV
from validator import validate
import pytest


def test_digits_01():
    assert Digits().check("123456")

    assert Digits().check("9876543210")

    assert Digits().check("0")

    assert Digits().check("1")

    assert Digits().check("-12345")


def test_digits_02():
    assert Digits().check("-9876543210")

    assert Digits().check("9876543210")

    assert not Digits().check("9876543abc")

    assert not Digits().check("12.34")

    assert not Digits().check("12345.67")

    assert not Digits().check("+")


def test_digits_03():
    assert not Digits().check("-")

    assert not Digits().check("1234abc")

    assert not Digits().check("0.0")

    assert not Digits().check("1.23")

    assert not Digits().check("12+34")


def test_digits_04_rpv():
    rpv = RPV("9876543210", [Digits()])
    assert rpv.execute()

    rpv = RPV("-123456", [Digits()])
    assert rpv.execute()

    rpv = RPV("abc123", [Digits()])
    assert not rpv.execute()

    rpv = RPV("123.45", [Digits()])
    assert not rpv.execute()


def test_digits_05_rpv():
    rpv = RPV("12345", [Digits()])
    assert rpv.execute()

    rpv = RPV("-12345", [Digits()])
    assert rpv.execute()

    rpv = RPV("12345abc", [Digits()])
    assert not rpv.execute()

    rpv = RPV("12.34", [Digits()])
    assert not rpv.execute()


def test_digits_06_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not Digits().check()

    # many arg
    with pytest.raises(TypeError):
        assert not Digits().check(5, 5, 5)

    # wrong type
    with pytest.raises(TypeError):
        assert not Digits().check("5", "5")


def test_digits_07_string():
    assert validate({"val": "123456"}, {"val": "digits"})

    assert validate({"val": "9876543210"}, {"val": "digits"})

    assert not validate({"val": "12345abc"}, {"val": "digits"})

    assert not validate({"val": "123.45"}, {"val": "digits"})


def test_digits_08_string():
    assert validate({"val": "12345"}, {"val": "digits"})

    assert validate({"val": "-98765"}, {"val": "digits"})

    assert not validate({"val": "12345abc"}, {"val": "digits"})

    assert not validate({"val": "123.45"}, {"val": "digits"})
