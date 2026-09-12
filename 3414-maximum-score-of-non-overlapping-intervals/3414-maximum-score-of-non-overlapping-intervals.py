class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[L, R, weight, i] for i, (L, R, weight) in enumerate(intervals)]
        n = len(intervals)

        # Sort intervals by right boundary
        intervals.sort(key=lambda x: x[1])

        # dp[k][i] = (score, indices) using at most k intervals among the first i intervals
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        # Pick interval i: weight[i] + best result from compatible intervals
        # Skip interval i: dp[k][i]
        for k in range(1, 5):
            for i in range(n):
                # Binary search for the last compatible interval
                L = 0
                R = i - 1

                # Exit the while loop when L > R
                while L <= R:
                    M = (L + R) // 2

                    if intervals[M][1] < intervals[i][0]:
                        L = M + 1
                    else:
                        R = M - 1

                # dp[k][i] = (score, indices)
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
