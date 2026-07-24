"""
Understand:
Provided a root node for BST and a key to delete in that BST
Find the node whose node.val equals key and attach the successor/predecessor node to that node
This could be successor or predecessor because they both won't break the BST tree
Return the root node

Match:
Binary search

Plan:
Use iterative to process the BST, find the node to delete first
and then attach the successor/predecessor node of that node if presents
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Return empy if root is empty
        if root is None:
            return None

        parent = None
        curr = root

        # Traverse through the BST to find the node that has key value
        while curr and curr.val != key:
            parent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # Return root if we didn't find the target node
        if curr is None:
            return root

        # Find the predecessor node and assign that node to our target node

        # If current node has two chldren, we find the predecessor,
        # which is the rightmost node in left subtree
        if curr.left and curr.right:
            # We use the same pattern as above, parent/curr
            # in this case is pred_parent/pred
            pred_parent = curr
            pred = curr.left

            # Exit the while loop after finding the predecessor
            while pred.right:
                pred_parent = pred
                pred = pred.right

            # Replace current node's value with predecessor's value
            # Note that we didn't replace curr.left/curr.right because
            # that is still correct
            curr.val = pred.val

            # Move curr/parent to pred/pred_parent
            curr = pred
            parent = pred_parent

        # If current node only has one child
        child = curr.left if curr.left else curr.right

        # If the target node is root node
        if parent is None:
            return child

        # Remove current node and attach child subtree
        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child

        return root


"""
Review:
I think the hardest part is to figure out how we can replace the target node without
breaking BST by using successor/predecessor. The trick of only copy over the value is 
interesting and worth remembering

Evaluate:
Instead of remembering successor/predecessor, I think what I need to know is the feature
of BST is how BST is constructed by boundary values, where as current node is bounded by left
subtree's biggest value and right subtree's smallest value.
"""
