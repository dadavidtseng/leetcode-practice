class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = s[i:j+1] 是否為 palindrome
        pal = [[False] * n for _ in range(n)]

        # 長度 1
        for i in range(n):
            pal[i][i] = True

        # 長度 2 ~ n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = s[0:i] 最多有幾個不重疊 palindrome
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # 不使用 s[i-1] 結尾的 palindrome
            dp[i] = dp[i - 1]

            # 找一個以 i-1 結尾的 palindrome
            for j in range(i - k + 1):
                if pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]