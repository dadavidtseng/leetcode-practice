class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curr_max = 1
        curr_min = 1

        for n in nums:
            (curr_max, curr_min) = (
                max(n, n * curr_max, n * curr_min),
                min(n, n * curr_max, n * curr_min),
            )
            result = max(result, curr_max)
        return result