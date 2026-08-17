# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return empty if root is empty
        if not root:
            return []

        result = []
        q = deque([root])  # Push root so the while loop can start

        # Exist when the queue is empty, which means that we've processed everything
        while q:
            # Cache the current level size from the queue
            # Note that we have to do this because q's size changes in the for loop below
            level_size = len(q)
            level = []

            # Iterate through the queue to process current level
            for _ in range(level_size):
                # Pop the front node and push its value into level
                front = q.popleft()
                level.append(front.val)

                # Push front node's children into queue if they exist
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

            # Push level into result because the level container
            # should now contain current level's nodes in right order
            result.append(level)
        return result
