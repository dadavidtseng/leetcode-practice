# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], left: int, right: int) -> bool:
            # Return true if current node is empty because we have nothing to check
            if not node:
                return True

            # Return false if current node is not valid for any of left/right bounds
            if not (left < node.val < right):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        # Note that TreeNode's value is int so we're using `float("inf")` to avoid the boundary problem
        return dfs(root, float("-inf"), float("inf"))
