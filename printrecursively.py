"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""
    # base case: if list is empty, return
    if not lst:
        return
    # print first element in list
    print(lst[0])
    # remove first element in list
    lst.remove(lst[0])
    # call function again until list is empty
    return print_recursively(lst)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. GREAT JOB!\n")
