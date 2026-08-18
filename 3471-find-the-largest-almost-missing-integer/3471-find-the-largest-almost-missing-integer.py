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


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        nums_size = len(nums)

        # If k is the size of nums,
        # return the maximum of nums because there is only one subarray
        if k == nums_size:
            return max(nums)

        # Create a frequency array for all possible integers
        # 0 <= nums[i] <= 50
        freq = [0] * 51

        for num in nums:
            freq[num] += 1

        # If k is 1,
        # that means we need to find the largest number in nums that appears exactly once,
        # so we iterate through freq from the largest num, which is 50
        # Return num if we find any, otherwise return -1
        if k == 1:
            for num in range(50, -1, -1):
                if freq[num] == 1:
                    return num
            return -1

        # If k is not the edge cases mentioned above, the almost missing integer would be either
        # from first or last element in nums.
        # Assign first/last to their value if they're valid
        # and return the maximum between first and last
        first = nums[0] if freq[nums[0]] == 1 else -1
        last = nums[-1] if freq[nums[-1]] == 1 else -1

        return max(first, last)


"""
Review:
I was able to get the idea of first and last element would be the answer, but I missed the edge cases of k=1 and k=nums_size. When planning out the implementation logic, I should consider the edge cases as well.

Evaluate:
By leveraging the constraints, I was able to use a simple for-loop to handle the edge cases k=nums_size. I think reading the constraints is great and essential when doing the understand part.

Complexity:
Time: O(n)
Space: O(1), 0 <= nums[i] <= 50 is considered constant instead of n
Where n is the length of the array
"""
