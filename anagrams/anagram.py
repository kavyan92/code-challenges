"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""

def make_anagram_dict(words):
    """Return dict mapping sorted letters -> [words w/ those letters]"""

    anagrams = {}
    # loop through list of words
    for word in words:
        # create key from alphabetically sorted word
        key = "".join(sorted(word))
        # add key to dict and word as value
        anagrams[key] = anagrams.get(key, []) + [word]

    return anagrams


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""
    # call helper function to create dict from wordlist
    anagrams = make_anagram_dict(wordlist)
    # find max length of values associated with a a key in the dict
    maximum = max(len(values) for values in anagrams.values())
    
    # loop through values to find first instance where max is hit
    for values in anagrams.values():
        if len(values) == maximum:
            # return first value in list of values
            return values[0]

all_words = [w.strip() for w in open('words.txt')]
find_most_anagrams_from_wordlist(all_words)





if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
