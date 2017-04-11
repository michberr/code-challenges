"""Print points in matrix, going in a spiral.

Give a square matrix, like this 4 x 4 matrix, it's composed
of points that are x, y points (top-left is 0, 0):

    0,0  0,1  0,2  0,3
    1,0  1,1  1,2  1,3
    2,0  2,1  2,2  2,3
    3,0  3,1  3,2  3,3

Starting at the top left, print the x and y coordinates of each
point, continuing in a spiral.

(Since we provide 3 different versions, you can change this to
the routine you want to test:


Here are different sizes:

    >>> spiral(1)
    (0, 0)

    >>> spiral(2)
    (0, 0)
    (0, 1)
    (1, 1)
    (1, 0)

    >>> spiral(3)
    (0, 0)
    (0, 1)
    (0, 2)
    (1, 2)
    (2, 2)
    (2, 1)
    (2, 0)
    (1, 0)
    (1, 1)

    >>> spiral(4)
    (0, 0)
    (0, 1)
    (0, 2)
    (0, 3)
    (1, 3)
    (2, 3)
    (3, 3)
    (3, 2)
    (3, 1)
    (3, 0)
    (2, 0)
    (1, 0)
    (1, 1)
    (1, 2)
    (2, 2)
    (2, 1)

"""


def heading(current, vx, vy, length):
    """Head in a direction with vx, vy from current for a given length"""

    for i in range(length-1):
            current = (current[0] + vx, current[1] + vy)
            print current

    return current


def spiral(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size.
    Use vectors as algorithm
    """

    box_size = matrix_size
    current = (0, 0)

    while box_size > 1:

        # Print corner of the box
        print current

        # Heading East
        current = heading(current, 0, 1, box_size)

        # Heading South
        current = heading(current, 1, 0, box_size)

        # Heading West
        current = heading(current, 0, -1, box_size)

        # Heading North
        # Go one less unit North than any other direction
        current = heading(current, -1, 0, box_size-1)

        # Slide current one unit to the East
        current = (current[0], current[1] + 1)

        # Deprecate box size by 2
        box_size -= 2

    # If matrix size is odd, we need to add in middle coordinate
    if matrix_size % 2 != 0:
        middle = matrix_size//2
        print (middle, middle)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n"
