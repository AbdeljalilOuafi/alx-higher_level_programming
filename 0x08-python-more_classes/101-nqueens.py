#!/usr/bin/python3
import sys


def solve_n_queens(N):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                    ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                    ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(ocuppied_positions, target_row, N):
        if target_row == N:
            result.append(ocuppied_positions)
            return
        for column in range(N):
            if can_place(column, ocuppied_positions):
                place_queen(ocuppied_positions + [column], target_row + 1, N)

    result = []
    place_queen([], 0, N)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])

