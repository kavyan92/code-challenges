"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    # base case: if list is empty, return 0
    if lst == []:
        return 0
    # add 1 for counter, and continue calling function until list is empty
    return 1 + count_recursively(lst[1:])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
