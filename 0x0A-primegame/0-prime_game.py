#!/usr/bin/python3
"""
This module determines the winner of a prime game.

Two players `Maria` and `Ben` play a game. Given a set of consecutive integers
starting from 1 up to and including `n`, they take turns choosing a prime
number from the set and remove that number and its multiples from the set. The
player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of the game is.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game.

    Args:
        x (int): number of rounds to be played.
        nums (list): array of `n`

    Returns:
        str: Returns the name of the player who has won the most rounds.
        None: Returns None if winner cannot be determined.
    """
    Maria = 0
    Ben = 0
    for round in range(x):
        # each round
        print(f'round {round}')
        roundNumber = nums[round]
        roundSet = [n for n in range(1, roundNumber+1)]
        count = 0

        # check for prime numbers
        for num in roundSet:
            if isPrime(num):
                notProducts = [i for i in roundSet if i % num != 0]
                roundSet = notProducts
                count += 1

        if (count % 2) == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben == Maria:
        return None
    return 'Maria' if Maria > Ben else 'Ben'


def isPrime(num):
    """ Checks if a number is a prime number."""
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        return True
    return False
