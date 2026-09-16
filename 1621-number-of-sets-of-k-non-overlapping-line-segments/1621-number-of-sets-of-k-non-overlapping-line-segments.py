# return comb(n + k - 1, 2 * k) % (10 ** 9 + 7)


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][state]
        # i = number of points processed
        # j = number of completed segments
        # state = 0: no open segment
        #         1: one open segment waiting for an endpoint
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(n):
            for j in range(k + 1):
                # 1. Skip point i
                dp[i + 1][j][0] += dp[i][j][0]
                dp[i + 1][j][1] += dp[i][j][1]

                # 2. Start a new segment at point i
                dp[i + 1][j][1] += dp[i][j][0]

                if j < k:

                    # 3. End current segment at point i
                    dp[i + 1][j + 1][0] += dp[i][j][1]

                    # 4. End current segment and
                    #    start the next one at the same point
                    dp[i + 1][j + 1][1] += dp[i][j][1]

                dp[i + 1][j][0] %= MOD
                dp[i + 1][j][1] %= MOD

                if j < k:
                    dp[i + 1][j + 1][0] %= MOD
                    dp[i + 1][j + 1][1] %= MOD

        return dp[n][k][0]
