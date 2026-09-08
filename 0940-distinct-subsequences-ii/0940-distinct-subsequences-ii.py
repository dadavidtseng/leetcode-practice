class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)
        last = [-1] * 26

        for i in range(n - 1, -1, -1):
            idx = ord(s[i]) - ord("a")
            duplicated = 0 if last[idx] == -1 else dp[last[idx] + 1]
            dp[i] = (2 * dp[i + 1] - duplicated) % MOD
            last[idx] = i
        return (dp[0] - 1) % MOD
