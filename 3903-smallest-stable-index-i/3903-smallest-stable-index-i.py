class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        result = float("inf")
        curr_max = nums[0]
        

        # max(nums[:i]) - min(nums[i:]) <= k
        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])
            curr_min = float("inf")
            for j in range(i, len(nums)):
                curr_min = min(curr_min, nums[j]) 
            if curr_max - curr_min <= k:
                result = min(result, i)
            print(result, curr_max, curr_min)
        return result if result != float("inf") else -1