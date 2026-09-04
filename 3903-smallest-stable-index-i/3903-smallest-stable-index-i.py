class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf = [nums[-1]] * n
        pre = -1
        
        # max(nums[:i]) - min(nums[i:]) <= k
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        for i in range(n):
            pre = max(pre, nums[i])
            if pre - suf[i] <= k:
                return i
        return -1
