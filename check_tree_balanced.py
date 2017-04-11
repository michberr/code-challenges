class BinaryNode(object):
    """Node in a binary tree.

    >>> N = BinaryNode

    For a tree of 1 item:

        >>> tree1 = N(1)
        >>> tree1.is_balanced()
        True

    For a tree of 2 items:

      1
     /
    2

        >>> tree2 = N(1,
        ...           N(2))
        >>> tree2.is_balanced()
        True

    Three:

      1
     / \
    2   3

        >>> tree3 = N(1,
        ...           N(2), N(3))
        >>> tree3.is_balanced()
        True

    Four:

         1
        / \
       2   4
      /
     3

        >>> tree4 = N(1,
        ...           N(2,
        ...             N(3)),
        ...           N(4))
        >>> tree4.is_balanced()
        True

    Five:

         1
       /---\
      2     5
     / \
    3   4

        >>> tree5 = N(1,
        ...           N(2,
        ...             N(3), N(4)),
        ...           N(5))
        >>> tree5.is_balanced()
        True

    Imbalanced Four:

        1
       /
      2
     / \
    3   4

        >>> tree4i = N(1,
        ...            N(2,
        ...              N(3), N(4)))
        >>> tree4i.is_balanced()
        False

    Imbalanced Six:

        1
       / \
      2   6
     / \
    3   4
       /
      5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False




    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?

        A tree is balanced if 1) the depths of its child trees differ by no
        more than one and 2) this is true for EVERY subtree.

        """

        def _height(node):
            """Calculate the height of a node"""

            if not node:
                return 0

            return 1 + max(_height(node.left), _height(node.right))

        def _is_balanced(node):
            """Check if the subtree at a node is balanced"""

            # An empty node is always balanced
            if not node:
                return True

            # If the heights differ by more than 1, return False
            if abs(_height(node.left) - _height(node.right)) > 1:
                return False

            return _is_balanced(node.left) & _is_balanced(node.right)

        return _is_balanced(self)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
