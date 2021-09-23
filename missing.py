"""Given a list of numbers 1...max_num, find which one is missing in a list."""

"""Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

def missing_number(nums, max_num):
    ##### SOLUTION 1 #####
    # make nums array into a set for shorter lookup time
    nums = set(nums)
    # loop through range
    for num in range(1, max_num+1):
        # check if each number is in set, if not then return that value
        if num not in nums:
            return num

    ##### SOLUTION 2 #####
    # create list of values in range
    x = range(1, max_num+1)
    # get sum of that range of values
    y = sum(x)
    # get sum of nums list provided
    z = sum(nums)

    # subtract the sum of list provided from the sum of the range and that will give you the missing number
    return y - z



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
