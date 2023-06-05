#!/usr/bin/python3

"""Solves the N-queens puzzle. Determines all solutions."""

import sys

chessb = []

def init_chessb(n):
    """Initialize an `n`x`n` chessboard."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def chessb_deepcopy(chessb):
    """Return a deepcopy of a chessboard."""
    return [list(row) for row in chessb]

def get_solution(chessb):
    """Return the solved chessboard representation."""
    return [[r, q] for r in range(len(chessb)) for q in range(len(chessb)) if chessb[r][q] == "Q"]

def xout(chessb, row, col):
    """X out spots on the chessboard."""
    for q in range(col + 1, len(chessb)):
        chessb[row][q] = "x"
    for q in range(col - 1, -1, -1):
        chessb[row][q] = "x"
    for r in range(row + 1, len(chessb)):
        chessb[r][col] = "x"
    for r in range(row - 1, -1, -1):
        chessb[r][col] = "x"
    q = col + 1
    for r in range(row + 1, len(chessb)):
        if q >= len(chessb):
            break
        chessb[r][q] = "x"
        q += 1
    q = col - 1
    for r in range(row - 1, -1, -1):
        if q < 0:
            break
        chessb[r][q]
        q -= 1
    q = col + 1
    for r in range(row - 1, -1, -1):
        if q >= len(chessb):
            break
        chessb[r][q] = "x"
        q += 1
    q = col - 1
    for r in range(row + 1, len(chessb)):
        if q < 0:
            break
        chessb[r][q] = "x"
        q -= 1

def recursive_solve(chessb, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(chessb):
        solutions.append(get_solution(chessb))
        return solutions
    for q in range(len(chessb)):
        if chessb[row][q] == " ":
            tmp_chessb = chessb_deepcopy(chessb)
            tmp_chessb[row][q] = "Q"
            xout(tmp_chessb, row, q)
            solutions = recursive_solve(tmp_chessb, row + 1, queens + 1, solutions)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessb = init_chessb(int(sys.argv[1]))
    solutions = recursive_solve(chessb, 0, 0, [])
    for sol in solutions:
        print(sol)

