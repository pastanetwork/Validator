from validator.rules import AlphaNum
from validator.rule_pipe_validator import RulePipeValidator as RPV
import pytest

def test_alpha_num_01():
    assert AlphaNum().check("user123")

    assert not AlphaNum().check("user_name")

    assert not AlphaNum().check("username!")

def test_alpha_num_02():
    assert AlphaNum().check("12345")

    assert AlphaNum().check("abcDEF")

    assert not AlphaNum().check("user name")

def test_alpha_num_03():
    assert AlphaNum().check("username")

    assert AlphaNum().check("1234")

    assert not AlphaNum().check("user@name")

def test_alpha_num_04():
    rpv = RPV(data="user123", rules=[AlphaNum()])
    assert rpv.execute()

    rpv = RPV(data="user_name", rules=[AlphaNum()])
    assert not rpv.execute()

    rpv = RPV(data="username!", rules=[AlphaNum()])
    assert not rpv.execute()

def test_alpha_num_05():
    rpv = RPV(data="12345", rules=[AlphaNum()])
    assert rpv.execute()

    rpv = RPV(data="abcDEF", rules=[AlphaNum()])
    assert rpv.execute()

    rpv = RPV(data="user name", rules=[AlphaNum()])
    assert not rpv.execute()

def test_alpha_num_06_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not AlphaNum().check(0)

    # wrong type
    with pytest.raises(TypeError):
        assert not AlphaNum().check([1, 2, 3])

    # non-string input
    with pytest.raises(TypeError):
        assert not AlphaNum().check(12345)
