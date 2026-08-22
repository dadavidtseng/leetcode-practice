# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_size = len(inorder)
        pre_idx = 0
        m = {}

        # Iterate through inorder to create inorder's value to index map
        for i in range(inorder_size):
            m[inorder[i]] = i

        # subtree's range= [L, R]
        def dfs(L: int, R: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            # Return empty when L crosses R
            if L > R:
                return None

            # Get root node's value from preorder[preorder's index]
            # and then increment preorder's index
            root_val = preorder[pre_idx]
            pre_idx += 1

            # Create root node
            root = TreeNode(root_val)

            # Get the index of root node in inorder
            M = m[root_val]

            # inorder = (L, M - 1) | root | (M + 1, R)
            root.left = dfs(L, M - 1)
            root.right = dfs(M + 1, R)
            return root

        return dfs(0, inorder_size - 1)
