from validator import validate


def test_numeric_max_compares_the_value():
    assert validate({"val": "7"}, {"val": "numeric|max:10"})

    assert validate({"val": "10"}, {"val": "numeric|max:10"})

    assert not validate({"val": "100"}, {"val": "numeric|max:10"})

    assert not validate({"val": "10.5"}, {"val": "numeric|max:10"})


def test_numeric_min_compares_the_value():
    assert validate({"val": "3"}, {"val": "numeric|min:3"})

    assert not validate({"val": "2.9"}, {"val": "numeric|min:3"})

    assert not validate({"val": "-5"}, {"val": "numeric|min:0"})


def test_numeric_between_compares_the_value():
    assert validate({"val": "32"}, {"val": "numeric|between:1,64"})

    assert validate({"val": "1.5"}, {"val": "numeric|between:1,64"})

    assert not validate({"val": "65"}, {"val": "numeric|between:1,64"})

    assert not validate({"val": "0.5"}, {"val": "numeric|between:1,64"})


def test_numeric_size_compares_the_value():
    assert validate({"val": "3"}, {"val": "numeric|size:3"})

    assert validate({"val": "3.0"}, {"val": "numeric|size:3"})

    assert not validate({"val": "333"}, {"val": "numeric|size:3"})


def test_numeric_bounds_accept_python_numbers():
    assert validate({"val": 7.5}, {"val": "numeric|max:10"})

    assert not validate({"val": 11}, {"val": "numeric|max:10"})


def test_a_value_that_is_not_a_number_still_fails():
    assert not validate({"val": "abc"}, {"val": "numeric|max:10"})

    assert not validate({"val": "nan"}, {"val": "numeric|max:10"})


def test_without_numeric_the_length_is_still_compared():
    assert validate({"val": "100"}, {"val": "max:10"})

    assert validate({"val": "100"}, {"val": "string|max:10"})
