"""Test for math module."""
import pytest
from water_jug_problem.math import gcd


def test_gcd():
    """test gcd with common divisor"""
    result = gcd(2, 4)
    assert result == 2


def test_gcd_primes():
    """test gcd with prime numbers"""
    result = gcd(5, 3)
    assert result == 1


def test_gcd_zero():
    """test gcd with zero"""
    with pytest.raises(ValueError):
        gcd(0, 0)
