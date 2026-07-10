class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        elevation = [[float("inf")] * col_size for _ in range(row_size)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, righ
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))

        while min_heap:
            cost, row, col = heapq.heappop(min_heap)

            if row == row_size - 1 and col == col_size - 1:
                return cost

            for r, c in directions:
                neighbor_r = row + r
                neighbor_c = col + c

                if (
                    neighbor_r < 0
                    or neighbor_c < 0
                    or neighbor_r >= row_size
                    or neighbor_c >= col_size
                ):
                    continue
                new_cost = max(cost, grid[neighbor_r][neighbor_c])
                if new_cost < elevation[neighbor_r][neighbor_c]:
                    elevation[neighbor_r][neighbor_c] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor_r, neighbor_c))
