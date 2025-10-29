from validator.rules import Url
from validator import validate


def test_url_01():
    """Test valid URLs with different schemes"""
    assert Url().check("https://www.example.com")

    assert Url().check("http://example.com")

    assert Url().check("https://subdomain.example.com")

    assert Url().check("ftp://files.example.com")


def test_url_02():
    """Test valid URLs with paths and query strings"""
    assert Url().check("https://www.example.com/path/to/page")

    assert Url().check("http://example.com/path?query=value")

    assert Url().check("https://example.com/path?key1=value1&key2=value2")

    assert Url().check("http://example.com:8080/path")


def test_url_03():
    """Test valid URLs with localhost and IP addresses"""
    assert Url().check("http://localhost")

    assert Url().check("http://localhost:8080")

    assert Url().check("http://192.168.1.1")

    assert Url().check("https://127.0.0.1:3000")


def test_url_04():
    """Test invalid URLs"""
    assert not Url().check("not a url")

    assert not Url().check("example.com")

    assert not Url().check("www.example.com")

    assert not Url().check("htp://example.com")

    assert not Url().check("://example.com")

    assert not Url().check("http://")


def test_url_05_string():
    """Test URL validation using validate function"""
    assert validate({"website": "https://www.example.com"}, {"website": "url"})

    assert validate({"website": "http://example.com/path"}, {"website": "url"})

    assert not validate({"website": "not a url"}, {"website": "url"})

    assert not validate({"website": "example.com"}, {"website": "url"})
