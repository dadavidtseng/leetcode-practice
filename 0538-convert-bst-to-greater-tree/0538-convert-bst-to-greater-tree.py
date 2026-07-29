"""
Understand:
Provided a root node of a BST, return a Greater Tree's root node
A greater tree means every node is the sum over every previous node that has greater value than current node,
including current node.
Ex. pre=5,4,3,2,1, curr=2, new_curr=5+4+3+2=14

Match:
Binary search, Recursion

Plan:
We need to traverse the BST from the largest node and update the nodes as we go.
We can't do it the other way around because converting a BST to Greater Tree will 
make the original largest node the smallest and the original smallest node the largest

We could use recursive call to do a reverse inorder traversal to this BST
and carry the sum with us so we can replace node value as we go
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Current sum that we keep track of
        curr_sum = 0

        # Recursive call for
        # 1. Reverse inorder traversal
        # 2. Keep track of current sum
        # 3. Replace current node's value
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal curr_sum

            if node is None:
                return
            dfs(node.right)
            curr_sum += node.val
            node.val = curr_sum
            dfs(node.left)

        # Return greater tree's root node after calling dfs function
        dfs(root)
        return root

"""
Review:
It was hard to come up with "reverse inorder traversal" solution, but once I came up
with that, it wasn't hard to write the code logic. A tricky part for DFS is that if you
want to use a integer variable from outside the nested function, we have to use "nonlocal".
One way to go around this is to use a list `curr_sum = [0]` instead. This is because that python
only allows you to "mutate object", but not "rebind value" in the nested function.

Evaluate:
I'll probably want to do some related problems or try iterative DFS for this problem
to be able to come up with this solution without having to struggle.

Complexity:
-Time:  O(n)
-Space: O(n) for recursion stack
"""