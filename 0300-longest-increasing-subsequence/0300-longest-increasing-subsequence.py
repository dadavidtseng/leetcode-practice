class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_size = len(nums)
        dp = [1] * len(nums)

        for i in range(nums_size - 1, -1, -1):
            for j in range(i + 1, nums_size):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
