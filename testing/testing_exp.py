import pytest
import exp

def test_return_hi():
    excpected_return = "hi"
    result = exp.return_hi()
    assert result == excpected_return