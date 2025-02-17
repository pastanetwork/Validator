from validator.rules import Nullable
from validator import validate


def test_nullable_standalone():
    # Nullable accepts None values
    assert Nullable()(None)
    assert not Nullable()("")
    assert not Nullable()([])
    assert not Nullable()({})


def test_nullable_with_required():
    # Nullable + Required: allows None but rejects empty values
    assert validate({"val": None}, {"val": "nullable|required"})  # None is allowed
    assert validate({"val": "dqd"}, {"val": "nullable|required"})
    assert not validate({"val": ""}, {"val": "nullable|required"})
    assert not validate({"val": []}, {"val": "nullable|required"})
    assert not validate({"val": {}}, {"val": "nullable|required"})

    # Nullable + Required: accepts valid values
    assert validate({"val": "Some value"}, {"val": "nullable|required"})
    assert validate({"val": ["Non-empty list"]}, {"val": "nullable|required"})
    assert validate({"val": {"key": "value"}}, {"val": "nullable|required"})


def test_nullable_and_other_rules():
    # Combining Nullable with other rules (example with integer validation)
    assert validate({"val": None}, {"val": "nullable|integer"})  # None is allowed
    assert validate({"val": 123}, {"val": "nullable|integer"})  # Valid integer is allowed
    assert not validate({"val": "hg"}, {"val": "nullable|integer"})
