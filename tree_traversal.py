## Traversing tree problems


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def dfs_iter(self, name):
        """Search a tree for a node using depth-first-search and iteration
        This solution has O(n) runtime. Worst case, we have to visit every node

        >>> henri = Node("Henri")
        >>> nora = Node("Nora", [henri])
        >>> nick = Node("Nick")
        >>> janet = Node("Janet", [nick, nora])
        >>> al = Node("Al")
        >>> bob = Node("Bob")
        >>> jen = Node("Jen")
        >>> jessica = Node("Jessica", [al, bob, jen])
        >>> jane = Node("Jane", [jessica, janet])
        >>> output = jane.dfs_iter("Al")
        ['Jane', 'Janet', 'Nora', 'Henri', 'Nick', 'Jessica', 'Jen', 'Bob', 'Al']
        """
        # Not necessary for function, only for testing purposes
        visited = []

        to_visit = [self]

        while to_visit:

            # Use our to_visit list like a stack
            current = to_visit.pop()
            visited.append(current.name)

            if current.name == name:
                print visited
                return current

            to_visit.extend(current.children)

        # Return none if node not found
        return None

    def bfs_iter(self, name):
        """Search a tree for a node using breadth-first-search and iteration

        This has much worse runtime because everytime we pop the first element we
        have to recopy the list which is O(n). Therefore, this is O(n^2)

        >>> henri = Node("Henri")
        >>> nora = Node("Nora", [henri])
        >>> nick = Node("Nick")
        >>> janet = Node("Janet", [nick, nora])
        >>> al = Node("Al")
        >>> bob = Node("Bob")
        >>> jen = Node("Jen")
        >>> jessica = Node("Jessica", [al, bob, jen])
        >>> jane = Node("Jane", [jessica, janet])
        >>> output = jane.bfs_iter("Al")
        ['Jane', 'Jessica', 'Janet', 'Al']

        """
        # Not necessary for function, only for testing purposes
        visited = []

        to_visit = [self]

        while to_visit:

            # Use our to_visit list like a queue
            current = to_visit.pop(0)
            visited.append(current.name)

            if current.name == name:
                print visited
                return current

            to_visit.extend(current.children)

    def dfs_recursive(self, name, friends=[]):
        """Search a tree for a node using depth-first-search and recursion

        >>> henri = Node("Henri")
        >>> nora = Node("Nora", [henri])
        >>> nick = Node("Nick")
        >>> janet = Node("Janet", [nick, nora])
        >>> al = Node("Al")
        >>> bob = Node("Bob")
        >>> jen = Node("Jen")
        >>> jessica = Node("Jessica", [al, bob, jen])
        >>> jane = Node("Jane", [jessica, janet])
        >>> output = jane.dfs_recursive("Al")
        ['Jessica', 'Al']

        Note: this dfs goes down the left side. The iterative solution goes
        down the right side.
        """

        if self.name == name:
            print friends
            return self

        for child in self.children:
            friends.append(child.name)
            result = child.dfs_recursive(name, friends)
            if result:
                return result

        return None


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"
