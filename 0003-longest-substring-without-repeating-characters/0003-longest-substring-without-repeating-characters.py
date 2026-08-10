class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        L = 0
        result = 0

        # Extend right pointer if we haven't seen that character before
        for R in range(len(s)):
            # Move left pointer until charSet doesn't contain s[R]
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])
            result = max(result, R - L + 1)
        return result
