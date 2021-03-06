"""Return new list from items with duplicates removed.

For example::

    >>> deduped([1, 1, 1])
    [1]

Keep items in the order where they first appeared::

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

A list with no duplicates would return the same::

    >>> deduped([1, 2, 3])
    [1, 2, 3]

This should return a *new* list, not mutate the existing
list::

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

An empty list should return an empty list::

    >>> deduped([])
    []

"""
# create new empty list
# loop over given list 
    # if item not in new list, append


def deduped(items):
    """Return new list from items with duplicates removed."""

    deduped = []

    for item in items: #=> loop over items
        if item not in deduped: # = > loop over deduped to check for item
            deduped.append(item)

    return deduped
    
    # runtime O(n^2)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE NO DUPE!\n")
