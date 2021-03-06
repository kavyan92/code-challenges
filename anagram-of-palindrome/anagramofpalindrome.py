"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    temp = []

    for letter in word:
        if letter in temp:
            temp.remove(letter)
        else:
            temp.append(letter)
    
    if len(temp) > 1:
        return False
    else:
        return True

    # counter = {}
    # for letter in word:
    #     counter[letter] = counter.get(letter, 0) + 1
    # seen_an_odd = False
    # for value in counter.values():
    #     if value % 2 == 0:
    #         continue
    #     else:
    #         # we already saw an odd
    #         # return false
    #         if seen_an_odd == True:
    #             return False
    #         # we havent see odd before
    #         # seen an odd becomes true
    #         else:
    #             seen_an_odd = True
           
    # return True


    # counter = {}
    # for letter in word:
    #     counter[letter] = counter.get(letter, 0) + 1
    # seen_an_odd = False
    # for value in counter.values():
    #     if value % 2 != 0:
    #         if seen_an_odd == True:
    #             return False
    #         seen_an_odd = True
    # return True




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
