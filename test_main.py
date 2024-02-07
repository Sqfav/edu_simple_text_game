from main import is_number, get_input, input_checked
import pytest


def test_enter_is_numeric_true():
    assert is_number('1') == True

def test_enter_is_numeric_false():
    assert is_number('abc') == False

def test_get_input_no_correct(monkeypatch):
    inputs = iter(['abc', '1', '11'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(StopIteration):
        get_input([1, 10], [1, 2, 3])

def test_get_input_correct(monkeypatch):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert get_input([1, 10], []) == 1

def test_input_checked_in_array_and_in_range():
    assert input_checked('1', [1, 10], [1]) == False

def test_input_checked_not_in_array():
    assert input_checked('1', [1, 10], []) == True

def test_input_checked_not_in_range():
    assert input_checked('11', [1, 10], []) == False