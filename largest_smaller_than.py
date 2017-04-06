

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

    # Minimum and maximum indices
    min = 0
    max = len(nums) - 1

    while max - min > 0:

        # Bisect the list
        # We add one to bisect on the right side if list has an even length
        # For example a list of length 4 would get cut at index 2 instead of 1
        mid = ((max - min) + 1)/2 + min

        if nums[mid] > xnumber:
            max = mid - 1
        elif nums[mid] < xnumber:
            min = mid

        # Case when nums[mid] == xnumber
        else:
            return nums[mid-1]

    return nums[min]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A GENIUS!\n"
