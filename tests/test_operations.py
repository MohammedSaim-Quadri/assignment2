import pytest
from app.operations import addition, division, subtraction, multiplication

def test_addition_positive():
    assert addition(1,1) == 2
    assert addition(6,4) == 10
    assert addition(-10,5) == 5

def test_addition_negative():
    assert addition(-6,-4) == -10
    assert addition(-10,-5) == -15

def test_subtraction_positive():
    assert subtraction(1,1) == 0
    assert subtraction(5,3) == 2
    assert subtraction(6,4) == 2

def test_subtraction_negative():
    assert subtraction(-1,-1) == 0
    assert subtraction(-5,-3) == -2

def test_multiplication_positive():
    assert multiplication(2,3) == 6
    assert multiplication(6,4) == 24
    assert multiplication(-10,5) == -50

def test_multiplication_negative():
    assert multiplication(-2,-3) == 6
    assert multiplication(-1,-1) == 1

def test_division_positive():
    assert division(1,1) == 1
    assert division(6,3) == 2

def test_division_negative():
    assert division(-6,-3) == 2
    assert division(-1,-1) == 1
    
def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)
