# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], limit: int, is_left: bool) -> bool:
            # Return true if current node is empty because we have nothing to check
            if not node:
                return True

            # Compare differently based on the bool flag
            valid = node.val < limit if is_left else node.val > limit

            # Return false if invalid
            if not valid:
                return False

            return is_valid(node.left, limit, is_left) and is_valid(
                node.right, limit, is_left
            )

        def dfs(node: Optional[TreeNode]) -> bool:
            # Return true if current node is empty because we have nothing to check
            if not node:
                return True

            # Return false if any of the recursive call returns false
            if not is_valid(node.left, node.val, True) or not (
                is_valid(node.right, node.val, False)
            ):
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)
