# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        s = []

        # Exit the loop when current node is empty and the stack is empty
        while curr or len(s) != 0:
            # Exit the loop when current node is nullptr,
            # otherwise, push the current node into stack
            # and keep going left
            while curr:
                s.append(curr)
                curr = curr.left

            # 1. Get current node from the top of the stack
            # 2. Remove the visited node since we don't need it anymore
            # 3. Decrement k
            curr = s.pop()
            k -= 1

            # If k is 0, that mean we've reached our goal, return the current node's value
            if k == 0:
                return curr.val

            # Move the current node to its right
            curr = curr.right

        # Return -1 to satisfy the compiler
        # Note that we'll never reach this because 1 <= k <= n <= 10^4
        return -1
