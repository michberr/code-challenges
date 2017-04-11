"""Split astring by splitter and return list of splits.

This should work like that built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implemented that.

"""


def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    time complexity is O(n^2)
    space complexity is O(n^2) because worst case you'd have to
    split on every character and the list slicing
    """

    split_string = []

    length = len(splitter)

    i = 0
    prev_split = 0

    while i < len(astring):
        if astring[i:i+length] == splitter:
            split_string.append(astring[prev_split:i])
            i += length
            prev_split = i
        else:
            i += 1

    # Need to add the last split
    split_string.append(astring[prev_split:])

    return split_string


def split2(string, splitter):
    """Splits a string with a one character splitter"""

    # Split starts at index 0
    prev_split_idx = 0
    split_string = []

    for i in range(len(string)):
        if string[i] == splitter:
            split_string.append(string[prev_split_idx:i])
            prev_split_idx = i+1

    # Add the last split
    split_string.append(string[prev_split_idx:])

    return split_string



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
