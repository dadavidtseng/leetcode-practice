# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Return None if the root is None
        if not root:
            return None

        # Swap the left and right children node
        root.left, root.right = root.right, root.left

        # Recursive call for each left and right node
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the modified tree's root node
        return root
