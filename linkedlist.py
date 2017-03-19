# Reverse a linked list


class Node(object):
    """Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """LinkedList class"""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Print list as a string

        >>> LinkedList(Node('A')).as_string()
        A

        >>> LinkedList(Node('A', Node('B', Node('C')))).as_string()
        ABC

        """

        str = ""

        current_node = self.head

        while current_node:
            str += (current_node.data)
            current_node = current_node.next

        print str

    def reverse_in_place(self):
        """Reverses the list in place

        Test case 1: Single Node
        >>> ll = LinkedList(Node('A'))
        >>> ll.reverse_in_place()
        >>> ll.as_string()
        A

        Test case 2: Longer LinkedList
        >>> ll = LinkedList(Node('A', Node('B', Node('C'))))
        >>> ll.reverse_in_place()
        >>> ll.as_string()
        CBA

        """

        current_node = self.head
        prev_node = None

        while current_node:

            # Save the next node in memory
            next_node = current_node.next

            # Switch the arrow for the current node
            current_node.next = prev_node

            # The current node becomes the previous node
            prev_node = current_node

            # The next node (saved above) becomes the current node
            current_node = next_node

        # Switch the ll head
        self.head = prev_node

    def reverse_in_place_recursive(self):
        """Reverses the list in place

        >>> ll = LinkedList(Node('A', Node('B', Node('C'))))
        >>> ll.reverse_in_place_recursive()
        >>> ll.as_string()
        CBA

        """

        current_node = self.head
        prev_node = None

        def _reverse_rec(current, prev):

            if not current:
                return prev

            next = current.next
            current.next = prev
            prev = current
            current = next

            return _reverse_rec(current, prev)

        # update the head of the ll with each recursive call
        self.head = _reverse_rec(current_node, prev_node)

    @staticmethod
    def reverse_not_in_place(ll):
        """Reverses the list in place

        Test case 1: Single Node
        >>> ll = LinkedList(Node('A'))
        >>> ll_reversed = LinkedList.reverse_not_in_place(ll)
        >>> ll_reversed.as_string()
        A
        >>> ll.as_string()
        A

        Test case 2: Longer linked list
        >>> ll = LinkedList(Node('A', Node('B', Node('C'))))
        >>> ll_reversed = LinkedList.reverse_not_in_place(ll)
        >>> ll_reversed.as_string()
        CBA
        >>> ll.as_string()
        ABC

        """

        current_node = ll.head

        # Instantiate a new linked list
        ll_reversed = LinkedList()

        while current_node:
            # Iterate through each node, create a copy,
            # add to the new ll, and update the head

            node_copy = Node(current_node.data)
            old_head = ll_reversed.head
            ll_reversed.head = node_copy
            node_copy.next = old_head

            # move to next node in the original ll
            current_node = current_node.next

        return ll_reversed




##################################################

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
