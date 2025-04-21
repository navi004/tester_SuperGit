from reviewed_code import factorial
import pytest

def test_factorial_negative_number():
    assert factorial(-1) == "Factorial is not defined for negative numbers."
    assert factorial(-5) == "Factorial is not defined for negative numbers."

def test_factorial_zero_and_one():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_positive_numbers():
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_invalid_input():
    with pytest.raises(TypeError):
        factorial("a")
    with pytest.raises(TypeError):
        factorial(1.5)

def test_factorial_edge_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2

def test_factorial_type_checking():
    with pytest.raises(TypeError):
        factorial([1, 2, 3])
    with pytest.raises(TypeError):
        factorial({"a": 1})

def test_factorial_none_input():
    with pytest.raises(TypeError):
        factorial(None)