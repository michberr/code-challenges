

def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number.

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    8

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    32

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    -2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -7) is None
    True

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    32

    This has log(n) runtime

    """

    # Win fast
    if nums[-1] < xnumber:
        return nums[-1]

    # Fail fast
    if nums[0] > xnumber:
        return None

    while len(nums) > 1:
        mid = len(nums)/2
        if nums[mid] > xnumber:
            nums = nums[:mid]
        elif nums[mid] < xnumber:
            nums = nums[mid:]

        # nums[mid] == xnumber
        else:
            return nums[mid-1]

    return nums[0]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A GENIUS!\n"
