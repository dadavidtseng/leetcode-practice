class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        row_size = len(grid)
        col_size = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        q = deque()

        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 2:
                    q.append((row, col))

        while q:
            for _ in range(len(q)):
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
                    if grid[next_row][next_col] != 1:
                        continue

                    grid[next_row][next_col] = 2

                    q.append((next_row, next_col))
            if q:
                result += 1

        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 1:
                    return -1

        return result
