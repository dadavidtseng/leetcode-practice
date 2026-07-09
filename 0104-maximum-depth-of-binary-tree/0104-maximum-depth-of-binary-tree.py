# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Return 0 if the root is None
        if not root:
            return 0

        # Recursively compute the depth of the left/right subtrees and add 1 for each of them
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        # Return the maximum from left/right depths as we unwind
        return max(left_depth, right_depth)
