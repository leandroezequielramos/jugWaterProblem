"""holds math functions"""

def gcd(a: int, b: int) -> int:
    """
    greater common divisor of two numbers a and b

    Parameters
    ----------
    a : int
        first number
    b : int
        second number_

    Returns
    -------
    int
       greater common divisor of a and b
    """
    assert(a >=0 and b >= 0)
    while b != 0:
        a, b = b, a % b
    return a