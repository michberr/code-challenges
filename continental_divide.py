"""
Given a matrix of altitudes, return the Continental Divide,
the set of coordinates where water can flow to both the Pacific and Atlantic.


    Ex 1:

    ~~Pac~~~~|
    ~~ 0 1 ~~
    ~~ 1 0 ~~
    |~~Atl~~~


    >>> matrix = [[0,1],[1,0]]
    >>> continental_divide(matrix)
    set([(0, 1), (1, 0), (0, 0), (1, 1)])


    Ex 2:

    ~~~~~~~~Pac~~~~~~~~|
    ~~ 1  2  2  3 (5) ~~
    ~~ 3  2  3 (4)(4) ~~
    ~~ 2  4 (5) 3  1  ~~
    ~~(6)(7) 1  4  5  ~~
    ~~(5) 1  1  2  4  ~~
    |~~~~~~~Atl~~~~~~~~~~

    >>> matrix = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
    >>> continental_divide(matrix)
    set([(1, 3), (3, 0), (3, 1), (1, 4), (0, 4), (0, 3), (4, 0)])

"""


def continental_divide(matrix):

    length = len(matrix)

    divide = set()

    # Iterate through each point and add to divide set if it can reach
    # the atlantic and the pacific
    for i in range(length):
        for j in range(length):

            coord = (i, j)
            # print "checking coordinate {}".format(coordinate)

            if can_reach_pacific(coord, matrix, length) and can_reach_atlantic(coord, matrix, length):

                divide.add(coord)

    return divide


def can_reach_pacific(coordinate, matrix, length, seen=set()):
    """Return boolean for whether a node can reach the Pacific"""

    # Winning case, stop recursing
    if is_on_pacific(coordinate):
        return True

    # If not on pacific, add the coordinate to seen set
    seen.add(coordinate)

    flow_neighbors = get_flow_neighbors(coordinate, matrix, length)

    # Recurse on each unseen neighbor where water can flow
    for neighbor in flow_neighbors - seen:

        if can_reach_pacific(neighbor, matrix, length, seen):
            return True

    # If we have recursed through all neighbors and not reached the pacific,
    # return False
    return False


def can_reach_atlantic(coordinate, matrix, length, seen=set()):
    """Return boolean for whether a node can reach the Atlantic"""

    if is_on_atlantic(coordinate, length):
        return True

    seen.add(coordinate)

    flow_neighbors = get_flow_neighbors(coordinate, matrix, length)

    for neighbor in flow_neighbors - seen:
        if can_reach_atlantic(neighbor, matrix, length, seen):
            return True

    return False


def is_on_pacific(coordinate):
    """Boolean for whether a point is on the Pacific"""

    return coordinate[0] == 0 or coordinate[1] == 0


def is_on_atlantic(coordinate, length):
    """Boolean for whether a point is on the atlantic"""

    return coordinate[0] == length-1 or coordinate[1] == length-1


def get_flow_neighbors(coordinate, matrix, length):
    """Return a set of the neighbors of a coordinate where water can flow"""

    neighbors = set()

    r, c = coordinate[0], coordinate[1]

    # Booleans for whether coordinates exist
    # to the left, right, above, and below the current
    left = c - 1 >= 0
    right = c + 1 < length
    above = r - 1 >= 0
    below = r + 1 < length

    # Add coordinate to the left
    if left:
        if can_flow(coordinate, (r, c-1), matrix):
            neighbors.add((r, c-1))

    # Add coordinate to the right
    if right:
        if can_flow(coordinate, (r, c+1), matrix):
            neighbors.add((r, c+1))

    # Add coordinate above
    if above:
        if can_flow(coordinate, (r-1, c), matrix):
            neighbors.add((r-1, c))

    # Add coordinate below
    if below:
        if can_flow(coordinate, (r+1, c), matrix):
            neighbors.add((r+1, c))

    # Add coordinate to upper-left
    if left and above:
        if can_flow(coordinate, (r-1, c-1), matrix):
            neighbors.add((r-1, c-1))

    # Add coordinate to upper-right
    if right and above:
        if can_flow(coordinate, (r-1, c+1), matrix):
            neighbors.add((r-1, c+1))

    # Add coordinate to bottom-left
    if left and below:
        if can_flow(coordinate, (r+1, c-1), matrix):
            neighbors.add((r+1, c-1))

    # Add coordinate to bottom-right
    if right and below:
        if can_flow(coordinate, (r+1, c+1), matrix):
            neighbors.add((r+1, c+1))

    return neighbors


def can_flow(curr_coord, test_coord, m):
    """Return boolean for whether water can flow from current to test coordinate"""

    return m[test_coord[0]][test_coord[1]] <= m[curr_coord[0]][curr_coord[1]]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"
