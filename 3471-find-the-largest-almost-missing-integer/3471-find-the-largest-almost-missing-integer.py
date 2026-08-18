"""
Understand:
Provided nums of integer array and a k of subarray size,
return the largetst integers that appears exactly once in all subarrays.

Match:
Array, Sliding Window

Plan:
Iterate through the nums and stop before the right pointer at the end of the array.
Use a result to keep track of the most seen integer that appears exactly once.
We could just iterate two subarrays from begin and end of the array because that's the only possibility.
"""

"""
3,9,7,2,1,7

"""


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        nums_size = len(nums)

        if k == nums_size:
            return max(nums)

        freq = [0] * 51

        for num in nums:
            freq[num] += 1

        if k == 1:
            for num in range(50, -1, -1):
                if freq[num] == 1:
                    return num
            return -1

        first = nums[0] if freq[nums[0]] == 1 else -1
        last = nums[-1] if freq[nums[-1]] == 1 else -1

        return max(first, last)
