def dec_to_binary(num):
    """Convert a number in decimal to binary

    >>> dec_to_binary(0)
    '0'

    >>> dec_to_binary(1)
    '1'

    >>> dec_to_binary(2)
    '10'

    >>> dec_to_binary(156)
    '10011100'

    Runtime of this solution is log2(n),
    because as num doubles in size, we only have to do
    on more iteration of each while loop

    """

    exponent = 0

    # Find 2^n, where n is the max exponent where 2^n < num
    while True:
        if 2**(exponent+1) > num:
            break

        exponent += 1

    # store num converted to binary
    binary_num = ""

    # Cycle back through powers of 2 in reverse.
    # For each power of 2, add a '1' to the
    # binary_num if it can be subtracted from num
    # and '0' if not
    while exponent >= 0:
        if num >= 2**exponent:
            num -= 2**exponent
            exponent -= 1
            binary_num += '1'
        else:
            exponent -= 1
            binary_num += '0'

    return binary_num


def dec_to_binary2(num):
    """Convert a number in decimal to binary

    >>> dec_to_binary2(0)
    '0'

    >>> dec_to_binary2(1)
    '1'

    >>> dec_to_binary2(2)
    '10'

    >>> dec_to_binary2(156)
    '10011100'

    Instead of first creating powers of 2, this solution
    divides the num successively by 2 and uses the remainders 
    to form the binary representation.

    Runtime of this solution is also log2(n),
    because as num doubles in size, we only have to do
    on more iteration of the while loop. It is however, faster
    than the first solution, because there is one less loop.

    """

    if num < 2:
        return str(num)

    else:

        binary_num = ""

        while num > 0:

            # Calculate the remainder and add to string
            binary_num = str(num % 2) + binary_num

            # Store the quotient as the new num
            num = num//2

        return binary_num


def dec_to_binary_recursively(num):
    """Convert a number in decimal to binary using recursion

    >>> dec_to_binary_recursively(0)
    '0'

    >>> dec_to_binary_recursively(1)
    '1'

    >>> dec_to_binary_recursively(2)
    '10'

    >>> dec_to_binary_recursively(156)
    '10011100'

    This solution also has runtime log2(n) and is the same
    speed as dec_to_binary2

    """

    if num < 2:
        return str(num)

    return dec_to_binary_recursively(num//2) + str(num % 2)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
