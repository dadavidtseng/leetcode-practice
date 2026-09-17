class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        dp = [float("inf")] * (n + 1)
        curr = 0
        L = 0
        result = float("inf")

        for R in range(len(arr)):
            curr += arr[R]

            while curr > target:
                curr -= arr[L]
                L += 1

            dp[R + 1] = dp[R]

            if curr == target:
                length = R - L + 1
                if L > 0:
                    result = min(result, length + dp[L])
                dp[R + 1] = min(dp[R + 1], length)

        return -1 if result == float("inf") else result
