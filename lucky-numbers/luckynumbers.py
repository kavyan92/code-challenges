"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # create new empty list
    # create counter variable
    # append random num between one and 10
    # do this n times but only if num is unique
    # increment counter each time a number is appended

    lucky_nums = []
    counter = 0
    while counter < n:
        i = random.randint(1,10)
        if i not in lucky_nums:
            lucky_nums.append(i)
            counter += 1

    return lucky_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT!\n")
