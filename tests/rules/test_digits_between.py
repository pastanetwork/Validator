from validator.rules import DigitsBetween
from validator.rule_pipe_validator import RulePipeValidator as RPV
from validator import validate
import pytest


def test_digits_between_01():
    assert DigitsBetween(10, 15).check("1234567890")

    assert DigitsBetween(10, 15).check("12345678901")

    assert DigitsBetween(10, 15).check("123456789012345")

    assert not DigitsBetween(10, 15).check("12345abc")

    assert not DigitsBetween(10, 15).check("123")


def test_digits_between_02():
    assert DigitsBetween(5, 10).check("12345")

    assert DigitsBetween(5, 10).check("9876543210")

    assert not DigitsBetween(5, 10).check("1234")

    assert not DigitsBetween(5, 10).check("123456789012345")


def test_digits_between_03():
    assert DigitsBetween(2, 6).check("12345")

    assert not DigitsBetween(2, 6).check("1")

    assert not DigitsBetween(2, 6).check("123456789")

    assert not DigitsBetween(2, 6).check("abc123")


def test_digits_between_04():
    rpv = RPV(data="1234567890", rules=[DigitsBetween(10, 15)])
    assert rpv.execute()

    rpv = RPV(data="12345678901", rules=[DigitsBetween(10, 15)])
    assert rpv.execute()

    rpv = RPV(data="1234567890123456", rules=[DigitsBetween(10, 15)])
    assert not rpv.execute()

    rpv = RPV(data="abc123", rules=[DigitsBetween(10, 15)])
    assert not rpv.execute()


def test_digits_between_05():
    rpv = RPV(data="12345", rules=[DigitsBetween(5, 10)])
    assert rpv.execute()

    rpv = RPV(data="9876543210", rules=[DigitsBetween(5, 10)])
    assert rpv.execute()

    rpv = RPV(data="1234", rules=[DigitsBetween(5, 10)])
    assert not rpv.execute()

    rpv = RPV(data="123456789012345", rules=[DigitsBetween(5, 10)])
    assert not rpv.execute()


def test_digits_between_06():
    rpv = RPV(data="12345", rules=[DigitsBetween(5, 6)])
    assert rpv.execute()

    rpv = RPV(data="123456", rules=[DigitsBetween(5, 6)])
    assert rpv.execute()

    rpv = RPV(data="1234", rules=[DigitsBetween(5, 6)])
    assert not rpv.execute()

    rpv = RPV(data="1234567", rules=[DigitsBetween(5, 6)])
    assert not rpv.execute()


# implémenter les mauvais tests pour la classe digits_between
def test_digits_between_07_bad():
    # zéro argument
    with pytest.raises(TypeError):
        assert not DigitsBetween().check("12345")

    # trop d'arguments
    with pytest.raises(TypeError):
        assert DigitsBetween(5, 10, 15).check("123456")

    # mauvais type
    with pytest.raises(TypeError):
        assert not DigitsBetween("5", "10").check("12345")


def test_digits_between_08_string():
    assert validate({"val": "123456"}, {"val": "digits_between:5,6"})

    assert validate({"val": "9876543210"}, {"val": "digits_between:5,10"})

    assert not validate({"val": "12345abc"}, {"val": "digits_between:5,6"})

    assert not validate({"val": "123456789012345"}, {"val": "digits_between:5,10"})

    assert not validate({"val": "1234"}, {"val": "digits_between:5,10"})


def test_digits_between_09_string():
    assert validate({"val": "12345"}, {"val": "digits_between:5,5"})

    assert validate({"val": "987654"}, {"val": "digits_between:5,6"})

    assert not validate({"val": "123"}, {"val": "digits_between:5,6"})

    assert not validate({"val": "1234567890"}, {"val": "digits_between:5,6"})
