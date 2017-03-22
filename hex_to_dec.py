def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('1A')
    26

    >>> hex_convert('FFFF')
    65535

    """

    convert = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    dec = 0
    length = len(hex_in)

    for i in range(length):
        dec += 16**i * convert[hex_in[length - i - 1]]

    return dec

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
