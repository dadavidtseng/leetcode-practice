"""
Understanding:
nums: integer array, find the subarray from nums that contains the maximum sum
subarray: increasing order and contiguous

Model: resettable counter
Planning:
iterate nums while keep track of a counter
1. If current subarray is not in increasing order, reset counter
2. If current subarray's sum is greater than what we've seen, update result
"""

"""
nums = [10, 20, 30, 5, 10, 50]
        L                  R
L=0, R=0, result = 0
L=0, R=0, result = 10        
L=0, R=1, result = 10+20=30(30>10)
L=0, R=2, result = 10+20+30=60(60>30)
L=0, R=3, result = 60
L=3, R=3, result = 60(60>5)
L=3, R=4, result = 60(60>5+10)
L=3, R=5, result = 65(5+10+50>60)

Time: O(n)
Space: O(1)
"""


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr_sum = 0
            curr_sum += nums[i]
            result = max(result, curr_sum)
        return result
