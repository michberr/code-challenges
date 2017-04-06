def is_string_transposed(s1, s2):
    """Checks if two strings are the same
    except that two adjacent letters are swapped.

    >>> is_string_transposed("Maria", "Marai")
    True

    >>> is_string_transposed("Marin", "Marai")
    False

    >>> is_string_transposed("Mraia", "Maria")
    True

    >>> is_string_transposed("Mraai", "Maria")
    False

    """

    # Fail fast if lengths don't match
    if len(s1) != len(s2):
        return False

    i = 0
    n_swaps = 0

    while i < len(s1):
        if s1[i] != s2[i]:

            try:
                # Check for swap
                swap = s1[i] == s2[i+1] and s1[i+1] == s2[i]
            except IndexError:
                # Will throw an index error if at end of string
                return False

            if swap:
                n_swaps += 1
                i += 2
            else:
                return False

            # Only allow one swap in string
            if n_swaps > 1:
                return False
        else:
            i += 1

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
