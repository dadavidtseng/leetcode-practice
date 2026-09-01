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

        def get_max(node: Optional[TreeNode]) -> int:
            # return 0 if current node is empty
            if not node:
                return 0

            # Get left/right nodes from recursive call
            left = get_max(node.left)
            right = get_max(node.right)

            # Return current node's value + max(left, right) if current sum is positive
            return max(node.val + max(left, right), 0)

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal result

            # return if node is empty
            if not node:
                return

            # Get left/right from current nodes' left/right subtrees
            left = get_max(node.left)
            right = get_max(node.right)

            # Update result if left + root's value + right is greater than result
            result = max(result, left + node.val + right)

            # Pass in current node's left/right nodes into DFS call
            dfs(node.left)
            dfs(node.right)

        # Pass root into DFS call
        dfs(root)
        return result
