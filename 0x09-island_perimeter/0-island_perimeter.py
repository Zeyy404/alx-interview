#!/usr/bin/python3
"""module island_perimeter"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a grid.

    Args:
      grid: A 2D list of integers representing land (1) and water (0).

    Returns:
      The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
            if i == len(grid) - 1 or grid[i+1][j] == 0:
                perimeter += 1
            if j == 0 or grid[i][j-1] == 0:
                perimeter += 1
            if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                perimeter += 1

    return perimeter
