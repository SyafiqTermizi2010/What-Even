def is_even(number: int) -> bool:
    """
    Check if a given number is an even number.

    Returns
    -------
    True if given number is even
    """
    if type(number) == int:
        return (number % 2) == 0
    raise ValueError("Number must be an integer")


def is_odd(number: int) -> bool:
    """
    Check if a given number is an odd number.

    Returns
    -------
    True if given number is odd
    """
    return not is_even(number)
