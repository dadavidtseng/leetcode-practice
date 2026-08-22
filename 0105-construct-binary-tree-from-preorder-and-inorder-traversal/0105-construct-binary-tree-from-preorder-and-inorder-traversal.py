# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Return empty if any of preorder and inorder is empty
        # Note that this is the base case of DFS, not an early return
        if not preorder or not inorder:
            return None

        # Create root node using preorder[0]
        # because index 0 in preorder will always be the root of a subtree
        root = TreeNode(preorder[0])

        # Get preorder[0]'s index in inorder
        mid = inorder.index(preorder[0])

        # preorder = root | preLeft | preRight
        # inorder = inorderLeft | root | inorderLeft
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
