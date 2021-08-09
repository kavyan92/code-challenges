"""Reverse a string.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """

    # new_string = []
    # for char in range((len(astring)-1), -1, -1): #[c, b, a] #[2, 1, 0]
    #     new_string.append(astring[char])
    
    # return "".join(new_string)

    return astring[::-1]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
