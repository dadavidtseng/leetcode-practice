class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a map to store char and index
        m = {}
        L = 0
        result = 0

        # Extend right pointer and store it in the map
        # 1. Move left pointer over right pointer only if we've seen it before
        # 2. Store the index into right pointer's character in the map
        # 3. Update result to keep track of longest window(substring)
        for R in range(len(s)):
            c = s[R]

            if c in m:
                L = max(L, m[c] + 1)
            m[c] = R
            result = max(result, R - L + 1)
        return result
