# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0

        # Use inorder traversal for BST and decrement k as it goes
        # Note that result will be sorted naturally because of the nature of BST
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, result

            if node is None:
                return

            dfs(node.left)

            
            k -= 1

            if k == 0:
                result = node.val
                return

            dfs(node.right)

        dfs(root)

        # Return kth smallest element
        return result
