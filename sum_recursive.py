def sum_list(nums):
    """Sum the numbers in a list with recursion

    >>> sum_list([])
    0
    >>> sum_list([1])
    1
    >>> sum_list([1, 2, 3])
    6

    """

    if not nums:
        return 0

    return nums[-1] + sum_list(nums[:-1])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
