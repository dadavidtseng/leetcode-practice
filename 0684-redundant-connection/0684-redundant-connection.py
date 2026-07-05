class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edges_size = len(edges)
        in_degree = [0] * (edges_size + 1)
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            in_degree[u] += 1
            in_degree[v] += 1

        q = deque()

        for node in range(1, edges_size + 1):
            if in_degree[node] == 1:
                q.append(node)

        while q:
            leaf = q.popleft()

            for neighbor in graph[leaf]:
                graph[neighbor].remove(leaf)
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 1:
                    q.append(neighbor)

            graph[leaf].clear()
            in_degree[leaf] = 0

        s = set()

        for node in range(1, edges_size + 1):
            if in_degree[node] > 0:
                s.add(node)

        for u, v in reversed(edges):
            if u in s and v in s:
                return [u, v]

        return []
