def permutations(letters, perm=''):
    """Return permutations of letters

    There are n! permutations where n is the length of letters.
    For the first letter there are n possibilities, for the second
    letter that are n-1 possiblities, etc.

    The way this algorithm works is that the permutations of 'abc'
    can be thought of as:
    'a' + permutations('bc')
    'b' + permutations('ac')
    'c' + permutations('ab')
    Then, we call the function recursively on the 2-letter words to the right.

    >>> permutations('abc')
    abc
    acb
    bac
    bca
    cab
    cba

    """

    if len(letters) == 0:
        print perm

    else:
        for i in range(len(letters)):

            # letters[i] is added to the permutation and removed from letters
            permutations(letters[0:i] + letters[i+1:], perm + letters[i])


def sub_permutations(letters, k, perm=''):
    """Return permutations of letters with length k

    this is a nPk problem. The number of permutations is
    n!/(n-k)!

    >>> sub_permutations("agtc", 2)
    ag
    at
    ac
    ga
    gt
    gc
    ta
    tg
    tc
    ca
    cg
    ct

    """

    if len(perm) == k:
        print perm

    else:
        for i in range(len(letters)):
            sub_permutations(letters[0:i] + letters[i+1:], k, perm + letters[i])


def sub_permutations_with_reps(letters, k, perm=''):
    """Return permutations of letters with length k with repetitions allowed

    There are n^k permutations, because in each of the k slots there are
    n possibilities.

    >>> sub_permutations_with_reps('agtc', 2)
    aa
    ag
    at
    ac
    ga
    gg
    gt
    gc
    ta
    tg
    tt
    tc
    ca
    cg
    ct
    cc

    """

    if len(perm) == k:
        print perm

    else:
        for i in range(len(letters)):

            # letters is not mutated in this case because of repeats
            sub_permutations_with_reps(letters, k, perm + letters[i])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
