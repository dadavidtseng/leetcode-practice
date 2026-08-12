class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L = 0
        max_freq = 0
        result = 0

        # Extend the window by moving its right pointer
        # and record the max window size (R-L+1) as we go
        for R in range(len(s)):
            c = s[R]

            # Use a frequency map to keep track of the maxFreq for each distinguish character
            # Note that maxFreq may sometimes be inaccurate because we don't decrement it
            # We don't decrement maxFreq because we want to get the maximum window size
            freq[c] = freq.get(c, 0) + 1
            max_freq = max(max_freq, freq[c])

            # Remove the leftmost character from the frequency map as we shrink the window
            while (R - L + 1) - max_freq > k:
                freq[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)
        return result
