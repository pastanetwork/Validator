import pytest

from validator.rules import Boolean
from validator import validate

def test_boolean_01():
    assert Boolean().check(True)
    assert Boolean().check(False)
    assert Boolean().check("yes")
    assert Boolean().check("no")
    assert Boolean().check(1)
    assert Boolean().check(0)
    assert Boolean().check("on")
    assert Boolean().check("off")

def test_boolean_02():
    assert not Boolean().check(17)
    assert not Boolean().check("maybe")
    with pytest.raises(TypeError):
        assert not Boolean().check([True, False])
    with pytest.raises(TypeError):
        assert not Boolean().check({"isBoolean": True})
    assert not Boolean().check(3.14)
    assert not Boolean().check(None)

def test_boolean_03():
    assert validate({"val": True}, {"val": "boolean"})
    assert validate({"val": "yes"}, {"val": "boolean"})
    assert validate({"val": 0}, {"val": "boolean"})
    assert not validate({"val": 17}, {"val": "boolean"})
    assert not validate({"val": "hello"}, {"val": "boolean"})
    with pytest.raises(TypeError):
        assert not validate({"val": [1, 0]}, {"val": "boolean"})
    assert not validate({"val": None}, {"val": "boolean"})

def test_required_boolean():
    assert validate({"val": True}, {"val": "required|boolean"})
    assert validate({"val": "on"}, {"val": "required|boolean"})
    assert not validate({}, {"val": "required|boolean"})
    assert not validate({"val": None}, {"val": "required|boolean"})
    assert not validate({"val": 17}, {"val": "required|boolean"})
