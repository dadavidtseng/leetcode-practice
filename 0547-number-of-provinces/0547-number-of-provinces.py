"""
Understand:
Ex1: 
isConnected[0][1] = isConnected[1][0] = 1
isConnected[0][2] = 0
isConnected[1][2] = 0
isConnected[2][0] = 0
isConnected[2][1] = 0
return = 2
[
[1,1,0],
[1,1,0],
[0,0,1]
]
Ex2: 
isConnected[0][1] = 0
isConnected[0][2] = 0
isConnected[1][0] = 0
isConnected[1][2] = 0
isConnected[2][0] = 0
isConnected[2][1] = 0
return = 2
[
[1,0,0],
[0,1,0],
[0,0,1]
]

Plan:
Iterate through the nodes and perform a DFS call for it.
Increment the counter if we can finish the DFS call.
"""



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Create a list to mark if the node has been visited
        n = len(isConnected)
        result = 0
        visited = [False] * n

        # DFS
        def dfs(node: int) -> None:
            visited[node] = True

            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)

        # Iterate through every node
        for i in range(n):
            if not visited[i]:
                dfs(i)
                result += 1
        return result
            