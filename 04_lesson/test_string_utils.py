import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("     skypro", "skypro"),
    (" 123", "123"),
    ("     hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("python", "python"),
    ("", ""),
    ("    ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("PythonP", "P", True),
    ("SkyPro", "F", False),
    ("Course", "c", False),
    ("123", "3", True),
    ("Course of 2025", " ", True),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, , input_symbol, expected", [
    ("", "d", False),
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Python", "P", "ython"),
    ("TtestT", "t", "TesT"),
    ("Course of 2025", " ", "Courseof2025"),
    ("SkyPro", "yPr", "Sko"),
    ("home", "home", ""),
    ("123", "3", "12"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, , input_symbol, expected", [
    ("SkyPro", "Por", "SkyPro"),
    ("SkyPro", "", "SkyPro"),
    ("", "F", ""),
    ("     ", " ", ""),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
