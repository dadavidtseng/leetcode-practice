class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        nums_size = len(nums)

        if nums_size == 1:
            return 1

        seen_min = float("inf")
        seen_max = float("-inf")
        seen_min_idx = 0
        seen_max_idx = 0

        for i in range(nums_size):
            if nums[i] < seen_min:
                seen_min = nums[i]
                seen_min_idx = i
            if nums[i] > seen_max:
                seen_max = nums[i]
                seen_max_idx = i

        L = min(seen_min_idx, seen_max_idx)
        R = max(seen_min_idx, seen_max_idx)
        LL = R + 1
        RR = nums_size - L
        LR = (L + 1) + (nums_size - R)

        return min(LL, RR, LR)
