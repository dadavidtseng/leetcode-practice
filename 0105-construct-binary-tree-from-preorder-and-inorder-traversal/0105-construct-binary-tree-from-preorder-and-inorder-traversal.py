# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create preIdx and inIdx to keep track of where we are in preorder and inorder
        pre_idx = 0
        in_idx = 0

        # Note that we only care about preoder's size because we are building the tree using
        # preorder as boundary. For inorder, we use it to know whether we should build left/right
        # subtrees and that has nothing to do with its size.
        preorder_size = len(preorder)

        dummy = TreeNode(0, None)
        curr = dummy

        # Exit the while loop when eith preIdx or inIdx equal or greater than preorder's size
        while pre_idx < preorder_size and in_idx < preorder_size:
            # 1. Create a new node and have this new node points to current node's right
            # 2. Assign current node's right to the new node(create/pass the thread!)
            # 3. Move current node to its right
            # 4. Increment preorder index
            new_node = TreeNode(preorder[pre_idx], None, curr.right)
            curr.right = new_node
            curr = curr.right
            pre_idx += 1

            # Exit the while loop when current node's value is inorder[inIdx]
            # because that's the end of left subtree
            # 1. Create a new node and have this new node points to current node
            # 2. Assign current node's left to the new node
            # 3. Move current node to its left
            # 4. Increment preorder index
            while curr.val != inorder[in_idx]:
                new_node = TreeNode(preorder[pre_idx], None, curr)
                curr.left = new_node
                curr = curr.left
                pre_idx += 1

            # Increment inorder index so that inorder[inIdx] points to root node's value
            in_idx += 1

            # Exit the while loop when current node's right is empty or current node's right vaule
            # isn't root node in that subtree.
            # 1. Cache current node's right as root node using the thread we created when building
            # left subtree
            # 2. Remove the thread by assigning current node's right to empty
            # 3. Move current node back to root node(parent)
            # 4. Increment inorder index
            while curr.right and curr.right.val == inorder[in_idx]:
                root = curr.right
                curr.right = None
                curr = root
                in_idx += 1

        return dummy.right
