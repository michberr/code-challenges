
def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31)
    4

    """

    assert 0 < val < 101, "Val must be between 1-100"

    lower = 1
    upper = 100

    num_guesses = 1
    guess = 50

    while guess != val:

        if val > guess:
            lower = guess
        else:
            upper = guess

        num_guesses += 1
        guess = (upper - lower)/2 + lower

    return num_guesses


##################################################

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
