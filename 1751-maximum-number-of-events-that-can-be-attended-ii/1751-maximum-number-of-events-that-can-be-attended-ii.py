class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = [[L, R, weight, i] for i, (L, R, weight) in enumerate(events)]
        n = len(events)

        # Sort intervals by right boundary
        events.sort(key=lambda x: x[1])

        # dp[k][i] = (score, indices) using at most k intervals among the first i intervals
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

        # Pick interval i: weight[i] + best result from compatible intervals
        # Skip interval i: dp[k][i]
        for x in range(1, k + 1):
            for i in range(n):
                # Binary search for the last compatible interval
                L = 0
                R = i - 1

                # Exit the while loop when L > R
                while L <= R:
                    M = (L + R) // 2

                    if events[M][1] < events[i][0]:
                        L = M + 1
                    else:
                        R = M - 1

                # dp[k][i] = (score, indices)
                pick = events[i][2] + dp[x - 1][R + 1]
                skip = dp[x][i]
                dp[x][i + 1] = max(pick, skip)
        return dp[k][n]
