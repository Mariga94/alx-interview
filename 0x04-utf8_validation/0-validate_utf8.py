#!/usr/bin/python3

"""UTF-8 Validation Module"""


def validUTF8(data):
    """Determnines if a given data set represents
    a valid UTF-8 encoding
    Args:
      data (int): value to be checked
    Returns:
      True if the data is a valid UTF-8 encoding,
      else return False
    """

    MAX_NUMBER_OF_ONES = 4
    bits = to_bits(data)
    for byte in bits:
        # single byte char
        if byte[0] == 0:
            continue

        # multi-byte character
        amount = sum(byte)
        if amount <= 1:
            return False
        if amount >= MAX_NUMBER_OF_ONES:
            return False

        for _ in range(amount - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True


def to_bits(bytes):
    """Iterator"""
    NUMBER_OF_BITS_PER_BLOCK = 8
    for byte in bytes:
        num = []
        exp = 1 << NUMBER_OF_BITS_PER_BLOCK
        while exp:
            exp >>= 1
            num.append(bool(byte & exp))
        yield num
