# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Return true if root and subRoot are both empty
        if root is None and subRoot is None:
            return True

        # Return false if one of root and subRoot is not empty
        if root is None or subRoot is None:
            return False

        def serialize(node: Optional[TreeNode]) -> str:
            # Return "$#" if this node is empty
            if node is None:
                return "$#"

            # Return the serialized tree string after pushing node's left/right nodes into DFS
            return "$" + str(node.val) + serialize(node.left) + serialize(node.right)

        def build_lps(pattern: str) -> List[int]:
            pattern_length = len(pattern)
            lps = [0] * pattern_length

            for i in range(1, pattern_length):
                j = lps[i - 1]

                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1
                lps[i] = j
            return lps

        text = serialize(root)
        pattern = serialize(subRoot)
        text_length = len(text)
        pattern_length = len(pattern)

        # Build the LPS (failure) table for the pattern
        lps = build_lps(pattern)

        # Search for pattern in text
        j = 0

        for i in range(text_length):
            # While there's a mismatch, we fallback to the index that's already a match instead of
            # starting from 0
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]

            # Advance j if it's currently a match
            if text[i] == pattern[j]:
                j += 1

            # Return true if pattern is found in text
            if j == pattern_length:
                return True
        # Return false if nothing was found
        return False
