"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""

# create empty list
# make two lists: one for upper case characters and one for lower
# loop through txt 
# find corresponding character in libraries and 'shift' to the right
# add that character to new list
# join and return new list


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    upper_lib = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_lib = 'abcdefghijklmnopqrstuvwxyz'

    encoded_string = []
    for char in txt:
        if char.islower():
            i = lower_lib.find(char)
            # print(char)
            x = i + shift
            if x > 25:
                x = x - 26
            encoded_string.append(lower_lib[x])
        if char.isupper():
            i = upper_lib.find(char)
            x = i + shift
            if x > 25:
                x = x - 26
            encoded_string.append(upper_lib[x])
        if char.isalpha() == False:
            # print(char)
            encoded_string.append(char)
        
    return "".join(encoded_string)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
