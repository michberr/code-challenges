# Sudoku

def solve(board):
    """Return boolean for whether sudoku board is solvable"""

    if is_full(board):

        # If our board is full, return a boolean for validity
        return is_valid(board)

    # Get the square with the fewest number of options
    # This returns a tuple with the index as the first element
    # and the candidates as the second element
    current_square = get_square_with_fewest_options(board)

    # Extract the coordinates from the first element of the tuple
    row, col = current_square[0][0], current_square[0][1]

    # Extract the list of candidates from the second element
    candidates = current_square[1]

    for candidate in candidates:
        board[row][col] = candidate
        if solve(board):
            return True

        # We didn't win, so we reset that position to empty
        board[row][col] = 0

    return False


def is_full(board):
    """Check if board has a number in each cell"""

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return False

    return True


def is_valid(board):
    """Check if board is valid

    >>> board = [[5,3,4,6,7,8,9,1,2],
    ...          [6,7,2,1,9,5,3,4,8],
    ...          [1,9,8,3,4,2,5,6,7],
    ...          [8,5,9,7,6,1,4,2,3],
    ...          [4,2,6,8,5,3,7,9,1],
    ...          [7,1,3,9,2,4,8,5,6],
    ...          [9,6,1,5,3,7,2,8,4],
    ...          [2,8,7,4,1,9,6,3,5],
    ...          [3,4,5,2,8,6,1,7,9]]

    >>> is_valid(board)
    True

    There are two 9's in the third row:

    >>> board = [[5,3,4,6,7,8,9,1,2],
    ...          [6,7,2,1,9,5,3,4,8],
    ...          [1,9,9,3,4,2,5,6,7],
    ...          [8,5,9,7,6,1,4,2,3],
    ...          [4,2,6,8,5,3,7,9,1],
    ...          [7,1,3,9,2,4,8,5,6],
    ...          [9,6,1,5,3,7,2,8,4],
    ...          [2,8,7,4,1,9,6,3,5],
    ...          [3,4,5,2,8,6,1,7,9]]

    >>> is_valid(board)
    False

    """

    num_set = set(range(1, 10))

    # Check that each row contains all 9 numbers
    check_rows(board, num_set)

    # Check that each column contains all 9 numbers
    check_columns(board, num_set)

    # Check that each inner square contains all 9 numbers
    check_subboards(board, num_set)

    return True


def check_rows(board, num_set):
    """Check rows"""

    for row in range(len(board)):
        if set(board[row]) != num_set:
            return False


def check_columns(board, num_set):
    """Check columns"""

    for col in range(len(board)):
        col_set = set()
        for row in range(len(board)):
            col_set.add(board[row][col])

        if col_set != num_set:
            return False


def check_subboards(board, num_set):
    """Check subboards"""

    for sub_board_i in range(9):
        # There are 9 sub-boards which I've labelled from 0-8
        # going from left-to-right, top-to-bottom

        # Coordinates of the top left corner of each sub-board
        left_corner_row = sub_board_i//3
        left_corner_column = (sub_board_i % 3) * 3

        sub_board_set = set()

        # Add numbers at sub-board coordinates to the set
        for i in range(3):
            for j in range(3):
                sub_board_set.add(
                    board[left_corner_row + i][left_corner_column + j]
                )

        if sub_board_set != num_set:
            return False

    return True


def get_square_with_fewest_options(board):
    pass


#####################################################

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***ALL TESTS PASS!\n"


# dfs(Tree):

# if not tree:
#     return True

# if tree.data == data:
#     return tree

# for neighbor in tree.neighbors:
#     result = dfs(neighbor)
#     if result:
#         return result





# to_visit = [tree]

# while to_visit:
#     current = to_visit.pop()
#     if current == data:
#         return current
#     to_visit.extend([current.left, current.right])
