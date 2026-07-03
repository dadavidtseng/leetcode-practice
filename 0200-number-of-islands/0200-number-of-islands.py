class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        row_size = len(grid)
        col_size = len(grid[0])

        def bfs(row: int, col: int) -> None:
            q = deque()
            grid[row][col] = "0"
            q.append((row, col))

            while q:
                row, col = q.popleft()

                for r, c in directions:
                    new_row = r + row
                    new_col = c + col

                    if new_row < 0 or new_col < 0 or new_row >= row_size or new_col >= col_size:
                        continue
                    if grid[new_row][new_col] == "0":
                        continue

                    q.append((new_row, new_col))
                    grid[new_row][new_col] = "0"

        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == "1":
                    bfs(row, col)
                    result += 1
        return result