def powerset1(my_set):
    """ Return powerset

    >>> powerset1(set([1, 2, 3, 4]))
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

    >>> powerset1(set("ABCD"))
    [[], ['A'], ['C'], ['A', 'C'], ['B'], ['A', 'B'], ['C', 'B'], ['A', 'C', 'B'], ['D'], ['A', 'D'], ['C', 'D'], ['A', 'C', 'D'], ['B', 'D'], ['A', 'B', 'D'], ['C', 'B', 'D'], ['A', 'C', 'B', 'D']]
    """

    results = [[]]
    for item in my_set:
        sub_result = []
        for subset in results:
            sub_result.append(subset + [item])
        results.extend(sub_result)

    return results


def powerset2(my_set):
    """Return powerset

    >>> powerset2(set([1, 2, 3, 4]))
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

    >>> powerset2(set("ABCD"))
    [[], ['A'], ['C'], ['A', 'C'], ['B'], ['A', 'B'], ['C', 'B'], ['A', 'C', 'B'], ['D'], ['A', 'D'], ['C', 'D'], ['A', 'C', 'D'], ['B', 'D'], ['A', 'B', 'D'], ['C', 'B', 'D'], ['A', 'C', 'B', 'D']]

    """

    # the power set of the empty set has one element, the empty set
    result = [[]]
    for item in my_set:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [item] onto everything in the
        # previous power set)
        result.extend([subset + [item] for subset in result])
    return result




##############################################################



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
