#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Determines who is the winner
    Arguments:
        x (int): number of rounds
        nums (int): array of prime numbers
    Returns: winner
    """
    prime = 0
    notPrime = 0
    if nums and x > 0:
        for i in nums:
            if i > 0:
                if i % 2 == 0:
                    prime += 1
                else:
                    notPrime += 1
        if prime > notPrime:
            return "Maria"
        else:
            return "Ben"
    return None