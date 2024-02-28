import pytest

class ExpectedError(Exception):
    pass

def my_function():
    print("a")
    raise ExpectedError()

    print("b")

def test_my_function():
    with pytest.raises(Exception):
        my_function()