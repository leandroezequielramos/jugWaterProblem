"""holds math functions"""


def gcd(a: int, b: int) -> int:
    """
    greater common divisor of two numbers a and b

    Parameters
    ----------
    a : int
        first number
    b : int
        second number

    Returns
    -------
    int
       greater common divisor of a and b
    """
    if a <= 0 or b <= 0:
        raise ValueError("Values must be greater than zero")
    while b != 0:
        a, b = b, a % b
    return a
