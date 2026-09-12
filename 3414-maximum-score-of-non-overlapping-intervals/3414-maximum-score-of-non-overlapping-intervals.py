class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[L, R, weight, i] for i, (L, R, weight) in enumerate(intervals)]
        n = len(intervals)

        # Sort intervals by right boundary
        intervals.sort(key=lambda x: x[1])

        # Define dp[k][i], where picking k intervals from the prefix of intervals ending at i
        # dp[k][i] = (score, intervals)
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        # Pick i: intervals[i][2] + dp[k-1][j]
        # Don't pick i: dp[k][i-1]
        for k in range(1, 5):
            for i in range(n):
                L = 0
                R = i - 1

                while L <= R:
                    M = (L + R) // 2

                    if intervals[M][1] < intervals[i][0]:
                        L = M + 1
                    else:
                        R = M - 1

                pick = (
                    intervals[i][2] + dp[k - 1][R + 1][0],
                    sorted(dp[k - 1][R + 1][1] + [intervals[i][3]]),
                )

                skip = dp[k][i]

                if pick[0] > skip[0]:
                    dp[k][i + 1] = pick
                elif pick[0] < skip[0]:
                    dp[k][i + 1] = skip
                else:
                    dp[k][i + 1] = pick if pick[1] < skip[1] else skip
        return dp[4][n][1]
