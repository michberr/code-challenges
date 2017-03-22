"""Count employees in an org chart.

Our organization has the following org chart::

                    Jane
          Jessica          Janet
       Al  Bob  Jen     Nick  Nora
                                Henri

Let's make this chart::

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

And test our counting function::

    >>> henri.count_employees()
    0

    >>> nora.count_employees()
    1

    >>> jane.count_employees()
    8

We provide a non-recursive version, let's make sure that gives the same
answer::

    >>> jane.count_employees_nonrecursive()
    8
    >>> henri.count_employees_nonrecursive()
    0

"""


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """

        count = 0

        for child in self.children:
            count += 1 + child.count_employees()

        return count

    def count_employees_nonrecursive(self):

        count = 0

        # Deal with empty node case
        if self:
            to_visit = self.children
        else:
            return None

        while to_visit:
            current = to_visit.pop()
            count += 1
            to_visit.extend(current.children)

        return count



def count_employees_from_name(tree, name):
    """Return a count of how many employees this person manages given their name.

    Return a count of how many people that manager manages. This should
    include *everyone* under them, not just people who directly report to
    them.

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

    >>> count_employees_from_name(jane, "Henri")
    0
    >>> count_employees_from_name(jane, "Jane")
    8

    """

    # Deal with empty node case
    if tree:
        to_visit = [tree]
    else:
        return None

    while to_visit:
        current = to_visit.pop()

        # If we found our node, return the count of the subtree
        if current.name == name:
            return current.count_employees()

        to_visit.extend(current.children)

    return None


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"
