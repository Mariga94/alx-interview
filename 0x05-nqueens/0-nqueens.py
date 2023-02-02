#!/usr/bin/python3
"""Queen Modules"""
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    queens = sys.argv[1]

    try:
        queens = int(queens)
    except Exception:
        print("N must be a number")
        exit(1)

    if queens < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0]*queens for _ in range(queens)]

    def nqueens(queens):
        # if n is 0, solution found
        if queens == 0:
            return True
        for i in range(0, queens):
            for j in range(0, queens):
                '''checking if we can place a queen here or not
                queen will not be placed if the place is being attacked
                or already occupied'''
                if (not (is_attack(i, j))) and (board[i][j] != 1):
                    board[i][j] = 1
                    # recursion
                    # wether we can put the next queen with this arrangment or not
                    if nqueens(queens-1) == True:
                        return True
                    board[i][j] = 0

        return False

    def is_attack(i, j):
        # checking if there is a queen in row or column
        for k in range(0, queens):
            if board[i][k] == 1 or board[k][j] == 1:
                return True
        # checking diagonals
        for k in range(0, queens):
            for l in range(0, queens):
                if (k+l == i+j) or (k-l == i-j):
                    if board[k][l] == 1:
                        return True
        return False
