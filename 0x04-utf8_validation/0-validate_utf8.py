#!/usr/bin/env python3

def validUTF8(data):
    # Helper function to check if a byte is a valid UTF-8 continuation byte
    def isContinuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        num_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        if 1 <= num_bytes <= 4:
            for j in range(1, num_bytes):
                i += 1
                if i >= len(data) or not isContinuation(data[i]):
                    return False
        else:
            return False

        i += 1

    return True
