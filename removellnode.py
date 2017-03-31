"""Given a node in a linked list, remove it.

Remove this node from a linked list. Note that we do not have access to
any other nodes of the linked list, like the head or the tail.

Does not return anything; changes list in place.

For example::

    >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    >>> three_node = ll.next.next
    >>> three_node.remove_node()
    >>> ll.as_string()
    '1245'

It's possible to remove the first node::

    >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    >>> one_node = ll
    >>> one_node.remove_node()
    >>> ll.as_string()
    '2345'

This will never be asked to remove the tail node.
"""


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

    def remove_node(self):
        """Given a node in a linked list, remove it.

        Remove this node from a linked list. Note that we do not have access to
        any other nodes of the linked list, like the head or the tail.

        Does not return anything; changes list in place.
        """

        self.data = self.next.data
        self.next = self.next.next


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT!\n"
