# ===========================================
#  Challenge: Print the First 50 Fibonacci Numbers
# ===========================================

# Write a program that prints the first 50 numbers of the Fibonacci sequence
# starting from 0.
# - The Fibonacci series is composed of a sequence of numbers where
#   the next number is always the sum of the previous two.
#   0, 1, 1, 2, 3, 5, 8, 13...


def fibonacci_50():
  minus1, minus2 = 1, 0
  for _ in range(50):
    print(minus2)
    minus2, minus1 = minus1, minus2 + minus1

fibonacci_50()