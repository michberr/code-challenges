class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def dfs_recursive(self, name):
        """Search a tree for a node using depth-first-search and recursion"""

        if self.name == name:
            return self

        for child in self.children:
            result = child.dfs_recursive(name)
            if result:
                return result

        return None
