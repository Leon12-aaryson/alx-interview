#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result
n being impossible to achieve, return an integer
Return 0
"""


def minOperations(n):
    """
    In in exactly n H characters in the file, this returns the
    fewest number of operation need to result
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n = n / min_operations
        min_operations += 1
    return operations
