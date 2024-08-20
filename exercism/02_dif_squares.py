# Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.
#
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.
#
# The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.
#
# Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of
# the first ten natural numbers is 3025 - 385 = 2640.
#
# You are not expected to discover an efficient solution to this yourself from first principles; research is allowed,
# indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering.

import unittest


def square_sum(num: int) -> float:
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum ** 2


def sum_squares(num: int) -> float:
    sum = 0
    for i in range(num + 1):
        i = i ** 2
        sum += i
    return sum


def main() -> None:
    num = 10
    dif = square_sum(num) - sum_squares(num)
    print(dif)


if __name__ == "__main__":
    main()
