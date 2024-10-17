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


def isWinner(x, nums):
    """Returns: name of the player that won the most rounds"""
    if (not isinstance(x, int) or
            not isinstance(nums, list) or
            x <= 0 or len(nums) == 0):
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    player1_wins = player2_wins = 0

    for n in nums:
        curr_set = set(range(1, n + 1))
        turn = 0

        while True:
            avail_primes = [p for p in primes if p <= n and p in curr_set]
            if not avail_primes:
                if turn == 0:
                    player2_wins += 1
                else:
                    player1_wins += 1
                break

            chosen_prime = avail_primes[0]
            curr_set.remove(chosen_prime)
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                curr_set.discard(multiple)

            turn = 1 - turn

    if player1_wins > player2_wins:
        return "Maria"
    elif player2_wins > player1_wins:
        return "Ben"
    else:
        return None
