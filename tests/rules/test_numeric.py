from validator.rules import Numeric
from validator import validate


def test_numeric_01():
    assert Numeric().check("23")

    assert Numeric().check("0")

    assert Numeric().check("99999")

    assert Numeric().check("85189125")

    assert Numeric().check("-1")

    assert Numeric().check("-10000")

    assert Numeric().check("-161651651")

    assert Numeric().check("10.5")

    assert Numeric().check("-10.5")

    assert Numeric().check("3.14159")


def test_numeric_02():
    assert Numeric().check(23)

    assert Numeric().check(0)

    assert Numeric().check(99999)

    assert Numeric().check(85189125)

    assert Numeric().check(-1)

    assert Numeric().check(-10000)

    assert Numeric().check(-161651651)

    assert Numeric().check(10.5)

    assert Numeric().check(-10.5)

    assert Numeric().check(3.14159)


def test_numeric_03():
    assert not Numeric().check("-")

    assert not Numeric().check("hello")

    assert not Numeric().check("abc")

    assert not Numeric().check("10a")

    assert not Numeric().check("123abc")

    assert not Numeric().check("NaN")


def test_numeric_04():
    assert not Numeric().check([])

    assert not Numeric().check([0, 1, 2])

    assert not Numeric().check("string")

    assert not Numeric().check(None)

    assert not Numeric().check({"a": 2})

    assert not Numeric().check(__file__)


def test_numeric_05():
    assert validate({"val": 23}, {"val": "numeric"})

    assert validate({"val": 0}, {"val": "numeric"})

    assert validate({"val": -5.3}, {"val": "numeric"})

    assert validate({"val": "42"}, {"val": "numeric"})

    assert validate({"val": "10.5"}, {"val": "numeric"})

    assert not validate({"val": {}}, {"val": "numeric"})

    assert not validate({"val": [123, 5]}, {"val": "numeric"})

    assert not validate({"val": "string"}, {"val": "numeric"})

    assert not validate({"val": "abc"}, {"val": "numeric"})
