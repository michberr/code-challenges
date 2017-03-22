def count_recursively(lst):
    """Return number of items in a list, using recursion.

    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3

    """

    if not lst:
        return 0

    count = 1

    count += count_recursively(lst[1:])

    return count


def count_recursively2(lst):
    """Return number of items in a list, using recursion.

    >>> count_recursively2([])
    0

    >>> count_recursively2([1, 2, 3])
    3

    """

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])


##################################################

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
