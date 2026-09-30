class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            count = count + 1 if num else 0
            result = max(result, count)
        return result
