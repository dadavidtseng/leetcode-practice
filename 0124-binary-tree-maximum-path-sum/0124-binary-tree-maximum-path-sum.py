# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return 0 if root node is empty
        if not root:
            return 0

        # Initialize the result to a very small number for all negative nodes case
        # Note that this could be result = -1001 because -1000 <= Node.val <= 1000
        result = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal result

            # return 0 if node is empty
            if not node:
                return 0

            # Get left/right from the best chain of the left/right subtrees,
            # ignore if negative because it'll decrement the result
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Update result if left + node's value + right is greater than result
            result = max(result, left + node.val + right)

            # Return current node's value + whichever is greater among left and right
            return node.val + max(left, right)

        # Pass root into DFS call
        dfs(root)
        return result
