# factorial.py

def factorial(n: int) -> int:
    """
    Calculate factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): Non-negative integer

    Returns:
    int: factorial of n

    Raises:
    ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
