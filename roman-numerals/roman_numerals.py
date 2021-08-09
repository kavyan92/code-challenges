"""Converts positive integers to Roman numeral equivilant

Write a method that converts an integer to its Roman numeral equivalent,
i.e., 476 => 'CDLXXVI'.

For reference, these are the building blocks for how we
encode numbers with Roman numerals: I = 1, V = 5, X = 10, L = 50, C = 100,
D = 500, M = 1000.

For example::

    >>> to_roman(5)
    'V'

    >>> to_roman(467)
    'CCCCLXVII'

You should convert to "old-school Roman numerals", where subtraction isn't
used. So, for exmple, 4 is "IIII" and 9 is "VIIII"::

    >>> to_roman(99)
    'LXXXXVIIII'

You do not need to convert numbers over 4,999, or less than 1.

"""


ROMAN_DIGIT = {1: 'I',
               5: 'V',
               10: 'X',
               50: 'L',
               100: 'C',
               500: 'D',
               1000: 'M'}

def find_remainder(num, divisor, symbol, roman):
    multiple = num // divisor
    roman += multiple * symbol
    
    return num % divisor, roman

def to_roman(num):
    """Converts positive integers to Roman numeral equivalent using Old-school style."""

    if num != int(num) or num > 4999 or num < 1:
        raise ValueError("Cannot convert")

    roman = ''

    if num > 999:
        num, roman = find_remainder(num, 1000, 'M', roman)
    if num > 499:
        num = num % 500
        roman += 'D'
    if num > 99:
        num, roman = find_remainder(num, 100, 'C', roman)
    if num > 49:
        num = num % 50
        roman += 'L'
    if num > 9:
        num, roman = find_remainder(num, 10, 'X', roman)
    if num > 4:
        num = num % 5
        roman += ('V' + (num * 'I'))

    return roman   


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOOOO!\n")
