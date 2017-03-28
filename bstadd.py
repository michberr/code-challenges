"""

We'll start with this tree::

                4
           2         7
         1   3     5   8

like this::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(7, Node(5), Node(8))
    ... )


Adding 0 should end up on the far left::

                4
           2         7
         1   3     5   8
        0

like so::

    >>> t.insert(0)

    >>> t.left.left.left.data == 0
    True

    >>> t.left.left.right is None
    True


Adding 9 should end up on the far right::

                4
           2         7
         1   3     5   8
        0               9

like so::

    >>> t.insert(9)

    >>> t.right.right.right.data == 9
    True

    >>> t.right.right.left is None
    True


Adding 6 should end up to the right of the 5::

                4
           2         7
         1   3     5   8
        0           6   9

like so::

    >>> t.insert(6)

    >>> t.right.left.right.data == 6
    True

    >>> t.right.left.left is None
    True

"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        if self.left is None and self.right is None:
            return "<Node %s>" % self.data
        else:
            return "<Node %s l=%s r=%s>" % (self.data, self.left, self.right)

    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        if not self:
            return Node(new_data)

        if new_data < self.data:
            if self.left:
                self.left.insert(new_data)
            else:
                self.left = Node(new_data)
        else:
            if self.right:
                self.right.insert(new_data)
            else:
                self.right = Node(new_data)

    def insert_iter(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        if not self:
            return Node(new_data)

        current = self

        while True:
            if new_data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(new_data)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(new_data)
                    break


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NODES ADDED SUCCESSFULLY!\n"
