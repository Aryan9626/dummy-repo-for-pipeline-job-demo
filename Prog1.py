#!/usr/bin/python3

"""
This code calculates the sum of all numbers in a given list.

It raises a `ValueError` if the input list is empty, ensuring meaningful sum calculations.
"""

def summation(data):
    """
    This function takes a list of numbers as input and returns their sum.

    Args:
        data (list): A list of numbers.

    Returns:
        int: The sum of the numbers in the list.

    Raises:
        ValueError: If the input list is empty.
    """

    if not data:
        raise ValueError("The input list cannot be empty.")

    total_sum = sum(data)

    return total_sum
