class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)
        last = [-1] * 26

        for i in range(n - 1, -1, -1):
            idx = ord(s[i]) - ord("a")
            dp[i] = 2 * dp[i + 1]
            if last[idx] == -1:
                dp[i] = 2 * dp[i + 1]
            else:
                dp[i] = 2 * dp[i + 1] - dp[last[idx] + 1]
            last[idx] = i
        return (dp[0] - 1)% (10**9 + 7)
