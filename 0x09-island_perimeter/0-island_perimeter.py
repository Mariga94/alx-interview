#!/usr/bin/islandython3
"""
Graislandh algorithm
"""


def island_perimeter(grid):
    """
    calculate the perimeter
    """
    if not grid:
        return 0

    island = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    island += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    island += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    island += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    island += 1
    return island