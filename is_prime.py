def is_prime(num):
    """Return boolean for prime number

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True

    >>> is_prime(999)
    False

    """

    # Win fast
    if num == 2:
        return True

    # Lose fast
    if num == 0 or num == 1 or num % 2 == 0:
        return False

    # We only need to check off numbers from 3 to the square root of
    # the num. Factors LARGER than the square root must be paired with a factor
    # SMALLER than the square root to equal the number. Therefore,
    # we know we've already searched all the possibilities.
    # Really, we only need to check prime numbers from 3, but it's as much
    # work to figure out if a number is prime than to test if it's a factor

    floored_sqrt = int(num ** (0.5))

    for i in range(3, floored_sqrt, 2):
        if num % i == 0:
            return False

    return True


def n_primes(n):
    """Return a list of n prime numbers

    n_primes(3)

    """

    if n == 0:
        return []

    # Initialize primes list with 2
    primes = [2]
    # Initialize index at 3
    i = 3

    while len(primes) < n:

        if is_prime(i):
            primes.append(i)

        i += 2

    return primes



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
