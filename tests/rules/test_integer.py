from validator.rules import Integer
from validator import validate


def test_integer_01():
    assert Integer().check("23")

    assert Integer().check("0")

    assert Integer().check("99999")

    assert Integer().check("85189125")

    assert Integer().check("-1")

    assert Integer().check("-10000")

    assert Integer().check("-161651651")


def test_integer_02():
    assert Integer().check(23)

    assert Integer().check(0)

    assert Integer().check(99999)

    assert Integer().check(85189125)

    assert Integer().check(-1)

    assert Integer().check(-10000)

    assert Integer().check(-161651651)


def test_integer_03():
    assert not Integer().check("-")

    assert not Integer().check("9.1")

    assert not Integer().check("-0.0")

    assert not Integer().check("0.0")

    assert not Integer().check("10.0")

    assert not Integer().check("-10000.213")

    assert not Integer().check("-161651651.12312312312")


def test_integer_04():
    assert not Integer().check(9.1)

    assert not Integer().check(-0.0)

    assert not Integer().check(0.0)

    assert not Integer().check(10.0)

    assert not Integer().check(-10000.213)

    assert not Integer().check(-161651651.12312312312)


def test_integer_05():
    assert not Integer().check([])

    assert not Integer().check([0, 1, 2])

    assert not Integer().check("string")

    assert not Integer().check(None)

    assert not Integer().check({"a": 2})

    assert not Integer().check(__file__)


def test_integer_06_string():
    assert validate({"val": -63}, {"val": "integer"})

    assert validate({"val": 0}, {"val": "integer"})

    assert validate({"val": 5}, {"val": "integer"})

    assert validate({"val": "42"}, {"val": "integer"})

    assert not validate({"val": {}}, {"val": "integer"})

    assert not validate({"val": [123, 5]}, {"val": "integer"})

    assert not validate({"val": 2.3}, {"val": "integer"})


def test_integer_05_base_10_only():
    assert not Integer().check("ff")

    assert not Integer().check("abc")

    assert not Integer().check("a")

    assert not Integer().check("0x1f")

    assert not Integer().check("0b101")

    assert not Integer().check("0o17")

    assert not Integer().check("1e3")

    assert not Integer().check("1_000")

    assert not Integer().check("٣")

    assert Integer().check(" 7 ")

    assert Integer().check("+12")


def test_integer_06_bounds_use_the_base_10_value():
    assert not validate({"val": "a"}, {"val": "integer|between:1,64"})

    assert validate({"val": "64"}, {"val": "integer|between:1,64"})

    assert not validate({"val": "65"}, {"val": "integer|between:1,64"})

    assert validate({"val": "010"}, {"val": "integer|max:10"})
