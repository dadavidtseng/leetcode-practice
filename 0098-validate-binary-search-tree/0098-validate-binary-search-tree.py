# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Return true if root is empty
        if not root:
            return True

        # Create a queue that carries current node and left/right bounds
        # and push root into the queue so we can start the while loop
        q = deque([(root, float("-inf"), float("inf"))])

        # Exit the while loop when queue is empty
        while q:
            # Get the front node and remove it from the queue
            node, left, right = q.popleft()

            # Continue is current node is empty because we don't need to process it
            if not node:
                continue

            # Return false if current node is not valid for any of left/right bounds
            if not (left < node.val < right):
                return False

            q.append((node.left, left, node.val))
            q.append((node.right, node.val, right))

        # Return true if we've successfully processed all nodes in the BST
        return True
