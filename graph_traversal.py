class Node(object):
    """Graph Node class"""
    def __init__(self, data, adj):
        self.data = data
        self.adj = adj or set()


def are_connected_dfs(self, person1, person2):

    # Nodes to visist
    to_visit = [person1]

    # Nodes we've already seen
    seen = set(person1)

    while to_visit:
        person = to_visit.pop()
        if person == person2:
            return True

        else:
            seen.add(person)
            for friend in person.adjacent - seen:
                to_visit.append(friend)

    return False


def are_connected_bfs(self, person1, person2):

    # Nodes to visit
    to_visit = [person1]

    # Nodes we've already seen
    seen = set(person1)

    while to_visit:
        person = to_visit.pop(0)
        if person == person2:
            return True

        else:
            seen.add(person)
            for friend in person.adjacent - seen:
                to_visit.append(friend)

    return False


def are_connected_recursive(self, person1, person2, seen=None):

    if not seen:
        seen = set()

    if person1 == person2:
        return True

    seen.add(person1)

    for friend in person1.adjacent - seen:
        if are_connected_recursive(friend, person2):
            return True

    return False
