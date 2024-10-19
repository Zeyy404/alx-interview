#!/usr/bin/python3
"""isWinner module"""


def sieve_of_eratosthenes(max_num):
    """
    Function to find all primes up to
    a maximum number using Sieve of Eratosthenes
    """
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if is_prime[p]]


def precompute_winner(max_n):
    """
    Precompute the number of moves for each n
    and store the winner for each game.
    """
    if max_n < 2:
        return ["Ben"] * (max_n + 1)

    primes = sieve_of_eratosthenes(max_n)
    winners = [None] * (max_n + 1)
    moves = [0] * (max_n + 1)

    for prime in primes:
        for multiple in range(prime, max_n + 1, prime):
            moves[multiple] += 1

    for n in range(1, max_n + 1):
        if moves[n] % 2 == 0:
            winners[n] = "Ben"
        else:
            winners[n] = "Maria"

    return winners


def isWinner(x, nums):
    """Returns: name of the player that won the most rounds"""
    if (not isinstance(x, int) or
            not isinstance(nums, list) or
            x <= 0 or len(nums) == 0):
        return None

    max_n = max(nums)
    winners = precompute_winner(max_n)

    player1_wins = player2_wins = 0

    for n in nums:
        if winners[n] == "Maria":
            player1_wins += 1
        else:
            player2_wins += 1

    if player1_wins > player2_wins:
        return "Maria"
    elif player2_wins > player1_wins:
        return "Ben"
    else:
        return None
