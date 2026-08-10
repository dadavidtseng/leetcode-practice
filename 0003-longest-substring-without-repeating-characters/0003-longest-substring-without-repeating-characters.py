class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_size = len(s)
        result = 0

        # Iterate through every possible substring
        for i in range(s_size):
            char_set = set()
            for j in range(i, s_size):
                c = s[j]

                # Exit the for loop when encountering seen character
                if c in char_set:
                    break
                char_set.add(c)
                result = max(result, len(char_set))
        return result
