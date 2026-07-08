class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        result = []

        for start, end in tickets:
            heapq.heappush(graph[start], end)

        stack = ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(heapq.heappop(graph[stack[-1]]))
            result.append(stack.pop())

        result.reverse()
        return result
