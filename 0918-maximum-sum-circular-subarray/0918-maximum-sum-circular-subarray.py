class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        min_sum = nums[0]
        max_sum = nums[0]
        curr_min = 0
        curr_max = 0

        for n in nums:
            curr_max = max(n, curr_max + n)
            curr_min = min(n, curr_min + n)
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, nums_sum - min_sum) if max_sum >= 0 else max_sum
