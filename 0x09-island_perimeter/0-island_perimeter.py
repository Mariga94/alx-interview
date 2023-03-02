#!/usr/bin/python3
"""
Graph algorithm
"""
from collections import deque


def island_perimeter(matrix):
    # Check for an empty matrix/graph.
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and c in range(cols) and matrix[r][c] == 1 and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands
