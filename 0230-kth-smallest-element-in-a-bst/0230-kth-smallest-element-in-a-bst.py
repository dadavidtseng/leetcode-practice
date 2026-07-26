# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        # Exit the while loop when there's no more node to process
        while curr:
            # If current node doesn't have a left child,
            # 1. Decrement k
            # 2. Return current node's value if k is 0
            # 3. Move the current node to its right
            if curr.left is None:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right

            # If current node does have a left child
            else:
                # Assign that left child node as predecessor
                pred = curr.left

                # Find the predecessor node
                while pred.right and pred.right != curr:
                    pred = pred.right

                # If this is the first time we visit the predecessor
                # 1. Create a link back to current node so that the next time we visit we know where
                # the root is for inorder traversal
                # 2. Move the current node to its left
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left

                # If this is the second time we visit the predecessor,
                # it's time to go back to root node
                # 1. Rremove the link from predecessor to current node
                # 2. Move the current node to its right
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        # Return -1 to satisfy the compiler
        # Note that we'll never reach this because 1 <= k <= n <= 10^4
        return -1
