#!/usr/bin/python3
"""
N-Queens Problem Solver
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check if there is a queen in the same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(n):
    """
    Solve the N-Queens problem for a board of size N.
    """
    def backtrack(board, row):
        """
        Backtracking function to recursively explore solutions.
        """
        if row == n:
            # If all queens are placed, add the solution to the result
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # backtrack

    # Initialize an empty board
    board = [-1] * n
    solutions = []

    # Start the backtracking algorithm
    backtrack(board, 0)

    return solutions


def main():
    """
    Main function to handle user input and printing solutions.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    solutions = solve_n_queens(n)

    # Print each solution
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
