#!/usr/bin/python3
"""
Module to validate the utf encoding of characters
"""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if the byte starts a new UTF-8 character
        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If the byte is invalid according to UTF-8 rules, return False
            if num_bytes == 0:
                continue
            # If the number of bytes is more than 4 or 1, return False
            if num_bytes > 4 or num_bytes == 1:
                return False
        else:
            # If the byte doesn't start with 10, return False
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        # Decrement the number of bytes left in the current character
        num_bytes -= 1

    # If all bytes have been processed and num_bytes is 0, return True
    return num_bytes == 0
