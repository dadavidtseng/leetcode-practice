# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        # Brutally traverse through the BST and store every node's values in result
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # Sort result and return kth smallest element
        result.sort()
        return result[k - 1]
