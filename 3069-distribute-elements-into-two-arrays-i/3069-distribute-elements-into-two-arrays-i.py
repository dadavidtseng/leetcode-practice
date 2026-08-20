"""
Understand
Match
Plan
"""


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for num in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[num])
            else:
                arr2.append(nums[num])
        return arr1 + arr2


"""
Result
Evaluate
"""
