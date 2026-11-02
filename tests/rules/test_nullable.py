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


def test_nullable_accepts_an_empty_string():
    assert validate({"val": ""}, {"val": "nullable|integer"})
    assert validate({"val": ""}, {"val": "nullable|alpha_dash|max:128"})
    assert validate({"val": ""}, {"val": "string|nullable|in:public,experimental"})
    assert validate({"val": ""}, {"val": "nullable|url"})
    assert validate({"val": ""}, {"val": "nullable|regex:/^[0-9]+$/"})


def test_nullable_still_checks_a_value():
    assert not validate({"val": "x"}, {"val": "nullable|integer"})
    assert not validate({"val": "x"}, {"val": "string|nullable|in:public,experimental"})


def test_empty_string_without_nullable_is_unchanged():
    assert not validate({"val": ""}, {"val": "integer"})
    assert not validate({"val": ""}, {"val": "required|string"})
