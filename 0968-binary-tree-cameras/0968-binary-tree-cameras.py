# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = 0
        covered = {None}

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode] = None) -> None:
            nonlocal result
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (
                    parent is None
                    and node not in covered
                    or node.left not in covered
                    or node.right not in covered
                ):
                    result += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root)
        return result
