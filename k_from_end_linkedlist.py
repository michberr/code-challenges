class Node(object):
    """Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """LinkedList class"""

    def __init__(self, head=None):
        self.head = head

    def find_k_from_end(self, k):
        """Find kth from end element of linkedlist

        >>> ll = LinkedList(Node('A', Node('B', Node('C', Node('D')))))
        >>> one = ll.find_k_from_end(1)
        >>> one.data
        'D'
        >>> two = ll.find_k_from_end(2)
        >>> two.data
        'C'
        >>> four = ll.find_k_from_end(4)
        >>> four.data
        'A'
        >>> ll.find_k_from_end(6) is None
        True

        """

        p1 = self.head
        p2 = self.head

        for i in range(k):
            # Handles invalid k's (longer than list)
            if not p2:
                return None
            else:
                p2 = p2.next

        while p2:
            p1 = p1.next
            p2 = p2.next

        return p1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
