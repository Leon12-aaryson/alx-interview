#!/usr/bin/python3
"""
  def isWinner(x, nums):
      '''
          determines the winner
      '''
      if not nums or x < 1:
          return None
      max_num = max(nums)

      filter = [True for _ in range(max(max_num + 1, 2))]
      for i in range(2, int(pow(max_num, 0.5)) + 1):
          if not filter[i]:
              continue
          for j in range(i * i, max_num + 1, i):
              filter[j] = False
      filter[0] = filter[1] = False
      y = 0
      for i in range(len(filter)):
          if filter[i]:
              y += 1
          filter[i] = y
      player1 = 0
      for x in nums:
          player1 += filter[x] % 2 == 1
      if player1 * 2 == len(nums):
          return None
      if player1 * 2 > len(nums):
          return "Maria"
      return "Ben"
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on a given set of numbers
    and a threshold.

    Args:
        x (int): The threshold value.
        nums (list): List of integers representing the numbers.

    Returns:
        str or None: The name of the winner (either "Maria" or "Ben"), or None
        if no winner is determined.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # Sieve of Eratosthenes to generate prime numbers
    sieve = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            sieve[j] = False
    sieve[0] = sieve[1] = False
    y = 0
    for i in range(len(sieve)):
        if sieve[i]:
            y += 1
        sieve[i] = y

    # Counting the number of prime numbers for each player
    player1 = 0
    for x in nums:
        player1 += sieve[x] % 2 == 1

    # Determining the winner
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
