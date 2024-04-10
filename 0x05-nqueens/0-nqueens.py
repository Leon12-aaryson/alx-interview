#!/usr/bin/python3
'''
N-Queens implementation
'''
import sys


def generate_solutions(row, column):
    '''
    Generates all possible solutions for placing queens on an NxN chessboard.

    Args:
        - row: The current row to place a queen.
        - column: The total number of columns (size of the chessboard).

    Returns:
        A list of solutions, where each solution is represented
        as a list of queen positions.
    '''
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    '''
    Determines safe positions to place a queen in the current row.

    Args:
        - queen: The current row in which to place the queen.
        - column: The total number of columns (size of the chessboard).
        - prev_solution: The solutions generated so far.

    Returns:
        A list of safe positions to place the queen in the current row.
    '''
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    '''
    Checks if it's safe to place a queen in a specific position.

    Args:
        - q: The current row.
        - x: The column where the queen is to be placed.
        - array: The current solution array.

    Returns:
        True if it's safe to place the queen; False otherwise.
    '''
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))


def init():
    '''
    Initializes the script and obtains the size of the chessboard (N)
    from command-line arguments.

    Returns:
        The size of the chessboard.
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    '''
    Main logic of the script for solving the N-Queens problem.
    Generates and prints all possible solutions.
    '''
    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
