# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Return 0 if the root is None
        if not root:
            return 0

        result = 0

        # Create a queue to store nodes from root
        # and push the root node into the queue
        q = deque()
        q.append(root)

        # Exit the while loop when the queue is empty
        while q:
            # Iterate through every nodes in the queue,
            # which is the nodes in a level
            for _ in range(len(q)):
                # Get the node from the queue,
                # which is the very left node for this level
                # if this is the first iteration of the for loop
                node = q.popleft()

                # Push that node's left/right children into the queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Increment the result as we finished a level
            result += 1
        return result
