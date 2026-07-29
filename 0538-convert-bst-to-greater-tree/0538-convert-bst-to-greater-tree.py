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
        curr = root
        stack = []

        # Exit the while loop when the stack and curr are both empty
        while stack or curr:
            # Keep going right and push current node into stack
            while curr:
                stack.append(curr)
                curr = curr.right

            # Get current node from the stack
            curr = stack.pop()
            curr_sum += curr.val
            curr.val = curr_sum

            # Move curr to curr.left
            # Note that curr might be empty after this
            # If curr is empty, we just reassign curr from stack.pop() in the next iteration
            # If curr is not empty, we will go right in the next iteration
            curr = curr.left

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

Update, neetcode's testing framework was giving me `RecursionError: maximum recursion depth exceeded`
so I had to write an iterative DFS solution.

Complexity:
-Time:  O(n)
-Space: O(n)
"""
