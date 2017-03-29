class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?

        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )

        >>> t.is_valid()
        True

        >>> t = Node(4,
        ...       Node(2, Node(3), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )

        >>> t.is_valid()
        False

        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(1), Node(7))
        ... )

        >>> t.is_valid()
        False

        """

        def _isvalid(node, min, max):
            """Recursive helper function"""

            # base case
            # We've reached a leaf node, and have not found an invalid node yet
            if not node:
                return True

            if min and node.data < min:
                return False

            if max and node.data > max:
                return False

            return (_isvalid(node.left, min, node.data) and
                    _isvalid(node.right, node.data, max))

        return _isvalid(self, min=None, max=None)


##################################################

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
