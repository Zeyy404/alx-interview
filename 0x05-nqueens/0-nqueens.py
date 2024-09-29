#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    solution = [[row, col] for row, col in enumerate(board)]
    print(solution)


def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1


def nqueens(n):
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(-1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(-1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(-1)

    nqueens(N)
