"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    #split string at spaces
    phrase = phrase.split()
    #create empty dictionary
    word_count = {}
    #loop through phrase and add count of each word to dict
    for word in phrase:
        word_count[word] = word_count.get(word, 0) + 1
    
    sorted_values = sorted(word_count.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in word_count.keys():
            if word_count[k] == i:
                sorted_dict[k] = word_count[k]

    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
