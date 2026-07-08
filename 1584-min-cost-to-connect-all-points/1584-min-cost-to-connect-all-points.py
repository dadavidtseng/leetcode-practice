class Solution:
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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge = []
        n = len(points)
        dsu = self.DSU(n)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                edge.append((weight, i, j))

        result = 0
        for weight, i, j in sorted(edge):
            if dsu.union(i, j):
                result += weight

        return result
