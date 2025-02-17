from validator.rules import AlphaDash
from validator.rule_pipe_validator import RulePipeValidator as RPV
import pytest


def test_alpha_dash_01():
    assert AlphaDash().check("user_name-123")

    assert not AlphaDash().check("user@name")

    assert not AlphaDash().check("username!")


def test_alpha_dash_02():
    assert not AlphaDash().check("1234!")

    assert AlphaDash().check("test_123")

    assert not AlphaDash().check("test*123")


def test_alpha_dash_03():
    assert AlphaDash().check("user-name")

    assert AlphaDash().check("username")

    assert not AlphaDash().check("user name")


def test_alpha_dash_04():
    rpv = RPV(data="user_name-123", rules=[AlphaDash()])
    assert rpv.execute()

    rpv = RPV(data="user@name", rules=[AlphaDash()])
    assert not rpv.execute()

    rpv = RPV(data="username!", rules=[AlphaDash()])
    assert not rpv.execute()


def test_alpha_dash_05():
    rpv = RPV(data="test_123", rules=[AlphaDash()])
    assert rpv.execute()

    rpv = RPV(data="1234!", rules=[AlphaDash()])
    assert not rpv.execute()

    rpv = RPV(data="test*123", rules=[AlphaDash()])
    assert not rpv.execute()


def test_alpha_dash_06_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not AlphaDash().check(0)

    # wrong type
    with pytest.raises(TypeError):
        assert not AlphaDash().check([1, 2, 3])

    # non-string input
    with pytest.raises(TypeError):
        assert not AlphaDash().check(12345)
