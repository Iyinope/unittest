# test_fibonacci_pytest.py
import pytest
from fibonacci import fibonacci

def test_basic_values():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_large_value():
    assert fibonacci(20) == 6765

def test_negative_input():
    with pytest.raises(ValueError):
        fibonacci(-5)
