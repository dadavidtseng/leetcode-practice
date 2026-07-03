class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.is_island(grid, row, col):
                    result += 1

        return result

    def is_island(self, grid: List[List[str]], row: int, col: int) -> bool:
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        if grid[row][col] != "1":
            return False
        if grid[row][col] == "0":
            return False

        grid[row][col] = "0"

        self.is_island(grid, row - 1, col)
        self.is_island(grid, row + 1, col)
        self.is_island(grid, row, col - 1)
        self.is_island(grid, row, col + 1)

        return True
