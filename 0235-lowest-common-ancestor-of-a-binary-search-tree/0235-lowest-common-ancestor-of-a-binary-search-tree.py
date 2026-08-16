# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Return empty if any of root, p, and q is empty
        if not root or not p or not q:
            return None

        curr = root

        while curr:
            # If current node's value is greater than p's and q's value, go left
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left

            # If current node's value is less than p's and q's value, go right
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right

            # Return the lowest common ancestor
            else:
                return curr

        # This will never be reached because we've already checked if root/p/q are valid
        return None
