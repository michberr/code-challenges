def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

    """

    letters = {}

    for char in word:
        # Load the counts of each char into the dictionary
        letters[char] = letters.get(char, 0) + 1

    odd = False

    for count in letters.values():
        if count % 2 != 0:
            if odd:
                return False
            odd = True

    return True

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
