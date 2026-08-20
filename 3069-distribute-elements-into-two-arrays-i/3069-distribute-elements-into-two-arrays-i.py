"""
Understand
Provided an integer array nums, distribute it to two integer arrays and combine them.
When distributing, append nums[i] to array1 when the last element of array1 is greater than the last element of array2, otherwise, append nums[i] to array2.
Return array1 + array2

Match
Array

Plan
Create arr1 = nums[0] and arr2 = nums[1] for the first operation.
Iterate through nums and compares arr1[-1] and arr2[-1] and append to array following the rule.
Return arr1 + arr2
"""


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        A = ([nums[0]], [nums[1]])

        # Iterate through nums from index 2 to end
        for num in nums[2:]:
            # In bool, true = 1, false = 0
            A[A[0][-1] <= A[1][-1]].append(num)
        return A[0] + A[1]


"""
Result
This is an easy question, the tricky part was to refactor it to not use if-else check.

Evaluate
When solving problem, if I am more sensitive to 0 and 1, I should be able to think of this refacored version of solution.

Complexity:
Time: O(n)
Space: O(n)
"""
