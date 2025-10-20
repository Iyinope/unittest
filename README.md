# fibonacci.py

def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number.
    F(0) = 0, F(1) = 1, F(2) = 1, ...

    Parameters
    ----------
    n : int
        Index of Fibonacci number (must be >= 0)

    Returns
    -------
    int
        The n-th Fibonacci number.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
