class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        result = []

        for start, end in tickets:
            heapq.heappush(graph[start], end)

        def dfs(node: str):
            while graph[node]:
                neighbor = heapq.heappop(graph[node])
                dfs(neighbor)
            result.append(node)

        dfs("JFK")

        result.reverse()
        return result
