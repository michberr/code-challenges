def get_max_profit(lst):
    """Return max profit from yesterday's stocks

    >>> get_max_profit([3, 5])
    2

    >>> get_max_profit([10, 7, 5, 8, 11, 9])
    6

    """

    min_price = lst[0]
    max_profit = None

    for i in range(1, len(lst)):

        potential_profit = lst[i] - min_price

        if potential_profit > max_profit:
            max_profit = potential_profit

        if lst[i] < min_price:
            min_price = lst[i]

    return max_profit


def get_max_profit(lst):

    max_profit = None

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):

            profit = lst[j] - lst[i]

            if profit > max_profit:
                max_profit = profit

    return max_profit

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
