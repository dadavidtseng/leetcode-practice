class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = 0
        visited = [False] * n

        def dfs(node):
            visited[node]=True
            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                result += 1

        return result