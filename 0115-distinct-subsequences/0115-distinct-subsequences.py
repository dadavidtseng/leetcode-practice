class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        dp = [0] * n

        for i in range(len(s)):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    if j != 0:
                        dp[j] += dp[j - 1]
                    else:
                        dp[0] += 1
        return dp[-1]
