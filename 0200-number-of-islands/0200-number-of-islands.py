class DSU:
    def __init__(self, n: int) -> None:
        self.parent: List[int] = list(range(n))
        self.rank: List[int] = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True


class Solution:
    """
    Think of every land cell ('1') as its own separate island initially. When two land cells are
    adjacent (up, down, left, right), they actually belong to the same island, so we should merge
    them.

    Disjoint Set Union (Union-Find) helps us:
        - Quickly connect adjacent land cells
        - Avoid counting the same island multiple times

    Each successful merge reduces the total island count by 1.

    Note:
        O(m * n) time, O(m * n) space
        Where m is the number of rows and n is the number of columns in the grid.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        row_size = len(grid)
        col_size = len(grid[0])
        _dsu = DSU(row_size * col_size)

        def dsu(row: int, col: int) -> None:
            nonlocal result

            for r, c in directions:
                new_row = r + row
                new_col = c + col

                if (
                    new_row < 0
                    or new_col < 0
                    or new_row >= row_size
                    or new_col >= col_size
                ):
                    continue
                if grid[new_row][new_col] == "0":
                    continue

                if _dsu.union(row * col_size + col, new_row * col_size + new_col):
                    result -= 1

        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == "1":
                    result += 1
                    dsu(row, col)
        return result
