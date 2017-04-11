
class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)


def create_circular_list(length):
    head = Node(data=1)
    prev = head

    for i in range(2, length + 1):
        curr = Node(data=i)
        curr.prev = prev
        prev.next = curr
        prev = curr

    # Last node should point back to the head
    curr.next = head
    head.prev = curr

    # Return the end of the list to begin counting at the head
    return curr


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(10, 3)
    4

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(10, 1)
    10

    >>> find_survivor(41, 3)
    31

    """

    # Create circular linked list
    curr = create_circular_list(num_people)

    while curr.next != curr:

        # Traverse the linkedlist by kill_every steps
        for i in range(kill_every):
            curr = curr.next

        # Remove the node
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        # Set it back to previous to begin counting forward
        curr = curr.prev

    return curr.data


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
