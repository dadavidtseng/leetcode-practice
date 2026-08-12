class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        result = 0

        # For each distinguish character, maintain a sliding window to find out the max result
        for c in char_set:
            # count is count of c inside the window
            # L is the left pointer of the window
            count = 0
            L = 0

            # Extend the window by moving its right pointer
            # and record the max window size (R-L+1) as we go
            for R in range(len(s)):
                if s[R] == c:
                    count += 1

                # Shrink the window by moving its left pointer when that window is invalid
                # Decrement count if we encounter c when shrinking the window
                while (R - L + 1) - count > k:
                    if s[L] == c:
                        count -= 1
                    L += 1
                result = max(result, R - L + 1)
        return result
