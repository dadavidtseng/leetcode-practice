class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}

        # Iterate through every element to find target
        # Build num_index_map along the way
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in num_index_map:
                return [num_index_map[diff], i]
            num_index_map[nums[i]] = i
        return []