#!/usr/bin/python3

class SolveNQueens:

    def __init__(self, n):
        # Atributes and varibles
        self.n = n
        self.colSet = set()
        self.posDiagSet = set()
        self.negDiagSet = set()
        self.board = self.create_board()
        self.solution = []


    def create_board(self):
        return [[" "] * self.n for i in range(self.n)]

    def parse_solution(self, board):
        parsed_solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "Q":
                    parsed_solution.append([r, c])
                    break
        return (parsed_solution)

    def solve_by_backtracking(self, r):
        if r == self.n:
            parsed_solution = self.parse_solution(self.board)
            self.solution.append(parsed_solution)
            return
        for c in range(self.n):
            if c in self.colSet or (r+c) in self.posDiagSet or (r-c) in self.negDiagSet:
                continue

            self.colSet.add(c)
            self.posDiagSet.add(r + c)
            self.negDiagSet.add(r - c)

            self.board[r][c] = "Q"

            self.solve_by_backtracking(r + 1)

            self.colSet.remove(c)
            self.posDiagSet.remove(r + c)
            self.negDiagSet.remove(r - c)
            self.board[r][c] = " "

    def solve(self):
        self.solve_by_backtracking(0)
        return self.solution
