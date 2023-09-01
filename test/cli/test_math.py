"""Test for math module."""
from water_jug_problem.math import gcd


def test_gcd():
    result = gcd(2, 4)
    assert result == 2
