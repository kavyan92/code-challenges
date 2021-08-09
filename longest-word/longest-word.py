"""Return longest word in list of words.

For example::

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

"""


def find_longest_word(words):
    """Return longest word in list of words."""
    # create variable to keep track of length
    longest_word = ''
    # loop over list and update length variable if length of word is greater
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return len(longest_word)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE MAX!\n")
