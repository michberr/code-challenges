"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    # Fail fast
    if abs(len(w1) - len(w2)) > 1:
        return False

    i = 0

    while i < len(w1) and i < len(w2):
        if w1[i] != w2[i]:

            # Case where one letter is swapped
            if w1[i + 1:] == w2[i + 1:]:
                return True
            # Case where one letter is added to w1
            elif w1[i + 1:] == w2[i:]:
                return True
            # Case where one letter is deleted from w1
            elif w1[i:] == w2[i + 1:]:
                return True
            # Failure case
            else:
                return False
        else:
            i += 1

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
