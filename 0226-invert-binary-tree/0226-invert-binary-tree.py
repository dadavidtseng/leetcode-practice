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

        s = []
        s.append(root)

        # Exit the while loop when the stack is empty
        while s:
            # Get the node from the stack to process
            # and remove that node form the stack
            node: TreeNode = s.pop()

            # Swap the node's left and right children
            node.left, node.right = node.right, node.left

            # Push the swapped left and right children into the stack
            # for next procesing iteration in the while loop
            # Note that we only push existed child into the stack
            # because there's nothing to process if that child node doesn't exist
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        # Return the modified tree's root node
        return root
