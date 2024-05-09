#!/usr/bin/python3
'''
    Implementation of the solution to the
    Island Perimeter interview question
'''


def island_perimeter(grid):
    '''
    Function that finds the perimeter of the island in the grid.

    Args:
    grid (list of lists): A 2D grid representing the island where 1
    represents land and 0 represents water.

    Returns:
    int: The perimeter of the island.
    '''
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Count all 4 sides initially

                # Check adjacent cells and subtract if neighbor is land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


if __name__ == "__main__":
    pass
