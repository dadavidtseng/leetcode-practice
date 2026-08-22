# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_size = len(preorder)
        pre_idx = 0
        in_idx = 0

        def dfs(limit: Optional[int]) -> Optional[TreeNode]:
            nonlocal pre_idx
            nonlocal in_idx

            # Return empty if we've processed all elements in preorder
            if pre_idx >= preorder_size:
                return None

            # If there's a limit and the value of that limit equals current element in inorder
            # 1. Increment inorder's index
            # 2. Return empty
            if limit is not None and limit == inorder[in_idx]:
                in_idx += 1
                return None

            # Get root node's value from preorder[preorder's index]
            # and then increment preorder's index
            root_val = preorder[pre_idx]
            pre_idx += 1

            # Create root node
            root = TreeNode(root_val)

            # Pass in new limit for left/right subtrees for DFS call
            root.left = dfs(root_val)
            root.right = dfs(limit)
            return root

        # Start the DFS call with no limit
        return dfs(None)
