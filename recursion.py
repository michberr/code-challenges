# Some light recursion problems

def listsum(numList):
    """Return the sum of a list

    >>> listsum([1,2,3])
    6
    """

    if not numList:
        return 0

    return numList[0] + listsum(numList[1:])


def print_item(my_list, i=0):
    """Prints each item in a list recursively.
        >>> print_item([1, 2, 3])
        1
        2
        3
    """
    if i == len(my_list):
        return

    print my_list[i]

    print_item(my_list, i+1)


def print_item2(my_list):
    """Prints each item in a list recursively.
        >>> print_item2([1, 2, 3])
        1
        2
        3
    """

    if not my_list:
        return

    print my_list[0]

    print_item2(my_list[1:])


def reverse_string(str):
    """Reverses a string

    >>> reverse_string("cat")
    'tac'
    >>> reverse_string("")
    ''
    >>> reverse_string("a")
    'a'

    """

    if not str:
        return str

    return str[-1] + reverse_string(str[:-1])


def is_palindrome(str):
    """Returns boolean for is_palindrome

    >>> is_palindrome("")
    True

    >>> is_palindrome("a")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("cat")
    False

    """

    if len(str) <= 1:
        return True

    if str[0] != str[-1]:
        return False

    return is_palindrome(str[1:-1])


def recursive_index(needle, haystack, count=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> lst = ["hey", "there", "you"]
    >>> recursive_index("hey", lst)
    0
    >>> recursive_index("you", lst)
    2
    >>> recursive_index("porcupine", lst) is None
    True

    """

    if not haystack:
        return None

    if haystack[0] == needle:
        return count

    return recursive_index(needle, haystack[1:], count+1)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
