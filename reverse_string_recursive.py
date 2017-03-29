def reverse_string(str):
    """Reverse a string with recursion

    >>> reverse_string('cat')
    'tac'
    >>> reverse_string('')
    ''
    >>> reverse_string('a')
    'a'

    """

    if not str:
        return ''

    return str[-1] + reverse_string(str[:-1])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
