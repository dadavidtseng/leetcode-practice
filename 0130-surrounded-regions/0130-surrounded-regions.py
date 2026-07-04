class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row_size = len(board)
        col_size = len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(row, col):
            q = deque()
            q.append((row, col))

            while q:
                row, col = q.popleft()

                for r, c in directions:
                    next_row = row + r
                    next_col = col + c

                    if (
                        next_row < 0
                        or next_col < 0
                        or next_row >= row_size
                        or next_col >= col_size
                    ):
                        continue
                    if board[next_row][next_col] != "O":
                        continue

                    board[next_row][next_col] = "S"
                    q.append((next_row, next_col))

        for row in range(row_size):
            for col in range(col_size):
                if row == 0 or col == 0 or row == row_size - 1 or col == col_size - 1:
                    if board[row][col] == "O":
                        board[row][col] = "S"

        for row in range(row_size):
            for col in range(col_size):
                if row == 0 or col == 0 or row == row_size - 1 or col == col_size - 1:
                    if board[row][col] == "S":
                        bfs(row, col)

        for row in range(row_size):
            for col in range(col_size):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "S":
                    board[row][col] = "O"
