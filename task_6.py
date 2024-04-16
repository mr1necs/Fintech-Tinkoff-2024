class BoardCheker:
    def __init__(self, size, board):
        self.size = size
        self.board = board
        self.st = (-1, -1)
        self.end = (-1, -1)
        self.directions = {
            "K": {(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)},
            "G": {(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)}
        }
        self.visited = {"K": set(), "G": set()}

    def bfs(self):
        queue = [(self.st, "K")]
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                position, state = queue.pop(0)
                cur_i, cur_j = position
                for di, dj in self.directions[state]:
                    i, j = cur_i + di, cur_j + dj
                    if (
                        i < 0
                        or i >= self.size
                        or j < 0
                        or j >= self.size
                        or (i, j) in self.visited[state]
                    ):
                        continue
                    if (i, j) == self.end:
                        return distance
                    elif self.board[i][j] not in (".", "S"):
                        queue.append(((i, j), self.board[i][j]))
                        self.visited[self.board[i][j]].add((i, j))
                    else:
                        queue.append(((i, j), state))
                        self.visited[state].add((i, j))
        return -1

    def solve(self):
        for i in range(self.size):
            row = self.board[i]
            if "S" in row:
                self.st = (i, row.index("S"))
            elif "F" in row:
                self.end = (i, row.index("F"))

        return self.bfs()


size = int(input())
board = [input() for _ in range(size)]

solver = BoardCheker(size, board)
result = solver.solve()
print(result)
