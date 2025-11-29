'''
We usually refer to the entries of a two-dimensional list by their row and column, like below on the left. Another way is shown below on the right.

    (0, 0) (0, 1) (0, 2)       0 1 2
    (1, 0) (1, 1) (1, 2)       3 4 5
    (2, 0) (2, 1) (2, 2)       6 7 8

    (a) Write some code that translates from the left representation to the right one. The // and % operators will be useful. Be sure your code works for arrays of any size.
    (b) Write some code that translates from the right representation to the left one.
'''


def main() -> None:
    rows = 3
    cols = 3

    index = 7
    row, col = index_to_coords(index, cols)
    display_result(index, row, col)


def index_to_coords(index: int, num_cols: int) -> tuple[int, int]:
    '''
    Converts a linear index back into (row, col).

    row = index // num_cols
    col = index % num_cols

    Example (3×3 grid):
        7 -> (7//3, 7%3) -> (2, 1)
    '''
    row = index // num_cols
    col = index % num_cols
    return row, col


def display_result(index: int, row: int, col: int) -> None:
    print(f'index: {index} -> (row: {row}, col: {col})')


if __name__ == '__main__':
    main()