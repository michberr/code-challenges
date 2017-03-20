def add_to_zero(lst):
    """Return boolean for whether any two numbers in a list sum to 0

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1,3,0])
    True

    >>> add_to_zero([1,3,5,-3])
    True

    """

    # Initialize a set to store nums we've seen
    nums = set()

    for num in lst:
        if -num in nums or num == 0:
            return True
        nums.add(num)

    return False


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
