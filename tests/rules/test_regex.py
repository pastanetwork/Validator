from validator.rules import Regex
from validator import validate


def test_regex_01():
    assert Regex("c").check("abcdef")

    assert Regex("^foo$").check("foo")

    assert Regex("abc*").check("abccc")

    assert Regex("abc*").check("ab")

    assert Regex("gray|grey").check("gray")

    assert Regex("z{3,6}").check("zzzz")

    assert Regex("xyz$").check("abcxyz")


def test_regex_02():
    assert not Regex("^c").check("abcdef")

    assert not Regex("^foo$").check("foobar")

    assert not Regex("abc*").check("a")

    assert not Regex("gr[ae]y").check("groy")

    assert not Regex("z{3,6}").check("xyzzxy")

    assert not Regex("xyz$").check("xyzabc")


def test_regex_03_string():
    assert validate({"val": "abcdef"}, {"val": "regex:a"})

    assert validate({"val": "dcdcdc"}, {"val": "regex:(dc)*"})

    assert validate({"val": "dcdcdc"}, {"val": "required|regex:(dc|ab)*"})

    assert not validate({"val": "foobar"}, {"val": "regex:foo(baz|foo)$"})

    assert not validate({"val": "groy"}, {"val": "regex:gr[ae]y"})

    assert not validate({"val": "xyzabc"}, {"val": "regex:xyz$"})


def test_regex_04_with_commas():
    """Test regex patterns containing commas"""
    # Pattern with comma should not be split
    assert validate({"val": "1,2,3"}, {"val": "regex:^\\d+(,\\d+)*$"})

    assert validate({"val": "123"}, {"val": "regex:^\\d+(,\\d+)*$"})

    assert not validate({"val": "1,2,a"}, {"val": "regex:^\\d+(,\\d+)*$"})

    assert not validate({"val": "abc"}, {"val": "regex:^\\d+(,\\d+)*$"})

    # Combined with other rules
    assert validate({"val": "1,2,3"}, {"val": "nullable|string|regex:^\\d+(,\\d+)*$"})

    assert validate({"val": None}, {"val": "nullable|string|regex:^\\d+(,\\d+)*$"})


def test_regex_delimited():
    assert validate({"val": "server.jar"}, {"val": r"required|regex:/^([\w\d._-]+)(\.jar)$/"})
    assert not validate({"val": "bad name"}, {"val": r"required|regex:/^([\w\d._-]+)(\.jar)$/"})
    assert validate({"val": "a/b"}, {"val": r"regex:/^a\/b$/"})


def test_regex_delimited_flags():
    assert validate({"val": "FOO"}, {"val": "regex:/^foo$/i"})
    assert not validate({"val": "FOO"}, {"val": "regex:/^foo$/"})
    assert validate({"val": "a\nb"}, {"val": "regex:/^b$/m"})


def test_regex_delimited_with_comma_and_pipe():
    assert validate({"val": "1,2"}, {"val": r"nullable|string|regex:/^\d+(,\d+)*$/"})
    assert not validate({"val": "a"}, {"val": r"nullable|string|regex:/^\d+(,\d+)*$/"})
    assert validate({"val": "b"}, {"val": "regex:/^(a|b)$/|max:5"})
    assert not validate({"val": "bbbbbbb"}, {"val": "regex:/^(a|b+)$/|max:5"})


def test_regex_not_delimited_is_unchanged():
    assert Regex("/foo").check("/foo")
    assert Regex("/foo/bar").check("/foo/bar")
    assert not Regex("/foo/z").check("foo")


def test_regex_refuses_a_value_that_is_not_text():
    assert not validate({"val": 12}, {"val": "regex:^12$"})
    assert not validate({"val": None}, {"val": "regex:^12$"})
