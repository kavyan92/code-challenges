"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""

# def lemur(branches)
    # count = 0
    # i = 0

    # while i < len(branches) - 1
        # loop through branches list
            # i += 2
            # if branch[i] == 1 or i >= len(branches)
                # count += 1
                # i -= 1
            # count += 1

        # return count
            
        


def lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    count = 0
    i = 0

    while i < len(branches) - 1:
        i += 2
        if i >= len(branches) or branches[i] == 1:
            i -= 1
        count += 1
        
    return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")