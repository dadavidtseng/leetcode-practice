# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            # Return if current node is empty
            if not node:
                return

            # Push an empty container for this level if result's size equals depth
            if len(result) == depth:
                result.append([])

            # Push current node's value into result[depth]
            result[depth].append(node.val)

            # Recursive call with left/right nodes and (depth+1)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result
