# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # Return true if both nodes are empty
            if p is None and q is None:
                return True

            # If both nodes aren't empty and they have the same value,
            # push their left/right nodes into recursive call
            if p is not None and q is not None and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            # Return false if none of the above checks match
            return False

        # Return true if root and subRoot are both empty
        if root is None and subRoot is None:
            return True

        # Return false if one of root and subRoot is not empty
        if root is None or subRoot is None:
            return False

        # Return true if root and subRoot are the same tree
        if isSameTree(root, subRoot):
            return True

        # Push in root's left/right nodes into two recursive calls if root and subRoot are not the
        # same tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
