class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        L = 0
        count = 0
        result = ""

        for R in range(len(s)):
            if s[R] == "1":
                count += 1
            if count == k:
                while s[L] == "0":
                    L += 1
                candidate = s[L : R + 1]

                if (
                    not result
                    or len(candidate) < len(result)
                    or (len(candidate) == len(result) and candidate < result)
                ):
                    result = candidate
                L += 1
                count -= 1
        return result
