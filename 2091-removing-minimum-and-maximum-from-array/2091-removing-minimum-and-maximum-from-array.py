class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        nums_size = len(nums)
        min_idx = 0
        max_idx = 0

        # Iterate through nums to get min_idx and max_idx
        for i in range(nums_size):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        # Compute L and R from min_idx and max_idx
        L = min(min_idx, max_idx)
        R = max(min_idx, max_idx)

        # There will be three possibilities,
        # 1. Both on left side
        # 2. Both on right side
        # 3. L on left side and R on right side
        LL = R + 1
        RR = nums_size - L
        LR = (L + 1) + (nums_size - R)

        # Return the mininum of all possibilities
        return min(LL, RR, LR)
