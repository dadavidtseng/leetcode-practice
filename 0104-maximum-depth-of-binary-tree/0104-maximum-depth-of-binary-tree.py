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

        result = 0

        # Create a stack to store a tuple of node and depth
        # and push the root node with depth 1 into the stack
        s = []
        s.append((root, 1))

        # Exit the while loop when the stack is empty
        while s:
            # Get the current node and depth from the stack
            curr = s.pop()
            (node, depth) = curr

            # If that node exists,
            #   1. Push that node's left/right children and incremented depth into the stack
            #   2. Calculate the max depth
            if node:
                s.append((node.left, depth + 1))
                s.append((node.right, depth + 1))
                result = max(result, depth)
        return result