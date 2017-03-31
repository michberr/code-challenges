def longest_substring(str1, str2):
    """Return the longest substring and it's length from two string inputs

    >>> longest_substring("abchelloabc", "xyzhelloxyz")
    (5, 'hello')
    """

    mat = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    max_length = 0

    for i in range(len(str1)):
        for j in range(len(str2)):

            if str1[i] == str2[j]:
                mat[i][j] = mat[i-1][j-1] + 1

                if mat[i][j] > max_length:
                    max_length = mat[i][j]
                    max_length_index = i - max_length + 1

    return max_length, str1[max_length_index:max_length_index + max_length]


def longest_substring2(str1, str2):
    """Return the longest substring and it's length from two string inputs

    This code is optimized for memory. Rather than retaining the full matrix,
    we only keep track of the current row and the previous row

    >>> longest_substring2("abchelloabc", "xyzhelloxyz")
    (5, 'hello')
    """

    max_length = 0

    # previous row of 0's with j+1 columns
    prev = None

    # current row of 0's with j+1 columns
    curr = [0 for j in range(len(str2) + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):

            if str1[i] == str2[j]:
            # If a letter in str1 is equal to a letter in str2,
            # assign that cell as one plus the cell in the upper left
                curr[j] = prev[j-1] + 1

                if curr[j] > max_length:
                # If the amount is now bigger than max_length, update max_length
                    max_length = curr[j]
                    max_length_index = i - max_length + 1

        # Update curr and prev
        prev = curr
        curr = [0 for j in range(len(str2) + 1)]

    return max_length, str1[max_length_index:max_length_index + max_length]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
