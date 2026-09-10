# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def dfs(node: TreeNode) -> tuple[int, int]:
            nonlocal result

            if not node:
                return (0, 0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + node.val + right_sum
            curr_count = left_count + 1 + right_count

            if curr_sum // curr_count == node.val:
                result += 1
            return curr_sum, curr_count

        dfs(root)
        return result
