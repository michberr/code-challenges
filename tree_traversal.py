## Traversing tree problems

def dfs_iter(tree, data):
    """Search a tree for a node using depth-first-search and iteration

    This solution has O(n) runtime. Worst case, we have to visit every node.

    """

    to_visit = [tree]

    while to_visit:

        # Use our to_visit list like a stack
        current = to_visit.pop()

        if current.data == data:
            return current

        to_visit.extend(current.children)

    # Return none if node not found
    return None

def bfs_iter(tree, data):
    """Search a tree for a node using breadth-first-search and iteration

    This has much worse runtime because everytime we pop the first element we
    have to recopy the list which is O(n). Therefore, this is O(n^2)
    """

    to_visit = [tree]

    while to_visit:

        # Use our to_visit list like a queue
        current = to_visit.pop(0)

        if current.data == data:
            return current

        to_visit.extend(current.children)


