class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        s_size = len(s)

        def expand(L: int, R: int) -> int:
            count = 0

            while L >= 0 and R < s_size and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
            return count

        for idx in range(s_size):
            result += expand(idx, idx) + expand(idx, idx + 1)
        return result
