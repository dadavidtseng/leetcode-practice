class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            result += nums[i] * nums[i] if n % (i + 1) == 0 else 0
        return result
