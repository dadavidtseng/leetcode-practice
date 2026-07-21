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

        def z_function(s: str) -> List[int]:
            # 1. z[i] = length of the longest common prefix between s[i...] and s[0...]
            # 2. Maintain the rightmost Z-box [L, R), where s[L...R-1] == s[0...(R-L)-1]
            s_size = len(s)
            z = [0] * s_size
            L = 0
            R = 0

            # Compute z[i] for every suffix starting at i
            for i in range(1, s_size):
                # If i falls inside the current Z-box, we can reuse the previously computed
                # value at i - L. However, the match cannot extend beyond the current Z-box,
                # so we cap it at R - i.
                if i < R:
                    z[i] = min(R - i, z[i - L])

                # Try to extend the current match beyond the Z-box
                # z[i] is the current matched prefix length
                while i + z[i] < s_size and s[z[i]] == s[i + z[i]]:
                    z[i] += 1

                # If we extended farther than the current Z-box,
                # update it to the new rightmost Z-box
                if i + z[i] > R:
                    L = i
                    R = i + z[i]
            return z

        # 1. Serialize text from root
        # 2. Serialize pattern from subRoot
        # 3. Combine pattern, delimeter, and text
        # Z-function compares every suffix with the prefix of the combined string.
        # Therefore, we put pattern at the beginning so that z[i] tells us how much
        # the current suffix matches the pattern.
        text = serialize(root)
        pattern = serialize(subRoot)
        combined = pattern + "|" + text

        pattern_length = len(pattern)
        combined_length = len(combined)
        z = z_function(combined)

        # From patternLength + 1 to the end,
        # if z[i] equals patternLength, that means pattern is in text
        for i in range(pattern_length + 1, combined_length):
            if z[i] == pattern_length:
                return True
        return False