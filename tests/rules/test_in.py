from validator.rules import In
from validator.rule_pipe_validator import RulePipeValidator as RPV
from validator import validate
import pytest


def test_in_01():
    assert not In(["apple", "banana"]).check("orange")
    assert In(["apple", "banana"]).check("apple")


def test_in_02():
    assert not In([1, 2, 3]).check(4)
    assert In([1, 2, 3]).check(2)


def test_in_03():
    assert In(["a", "b", "c"]).check("b")
    assert not In(["x", "y", "z"]).check("a")


def test_in_04_rpv():
    rpv = RPV("yes", [In(["yes", "no"])])
    assert rpv.execute()

    rpv = RPV(10, [In([5, 10, 15])])
    assert rpv.execute()

    rpv = RPV("admin", [In(["admin", "user", "guest"])])
    assert rpv.execute()


def test_in_05_rpv():
    rpv = RPV("maybe", [In(["yes", "no"])])
    assert not rpv.execute()

    rpv = RPV(20, [In([5, 10, 15])])
    assert not rpv.execute()

    rpv = RPV("superadmin", [In(["admin", "user", "guest"])])
    assert not rpv.execute()


def test_in_06_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not In().check("test")

    # many args
    with pytest.raises(TypeError):
        assert not In(["yes", "no"], ["maybe"]).check("test")


def test_in_07_string():
    assert validate({"role": "admin"}, {"role": "in:admin,user,guest"})
    assert not validate({"role": "superadmin"}, {"role": "in:admin,user,guest"})


def test_in_08_string():
    assert validate({"status": "active"}, {"status": "in:active,inactive"})
    assert not validate({"status": "pending"}, {"status": "in:active,inactive"})


def test_in_09_string():
    assert validate({"forge_version": "recommended"}, {"forge_version" : "required|string|in:recommended,latest"})
    assert not validate({"forge_version": "neoforge"}, {"forge_version" : "required|string|in:recommended,latest"})