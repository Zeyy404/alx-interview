#!/usr/bin/python3
"""Minimum Operations"""
from math import sqrt


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly `n` "H" characters in the file
    """
    if n <= 1:
        return 0

    min_operation = n

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisor = i
            other_divisor = n // i

            oprt_with_divisor = minOperations(divisor) + (n // divisor)
            min_operation = min(oprt_with_divisor, min_operation)

            oprt_with_other_divisor = minOperations(other_divisor) + (divisor)
            min_operation = min(oprt_with_other_divisor, min_operation)

    return min_operation
