class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        R = 0

        while R < len(nums):
            if nums[R] != val:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1                
            R += 1
        return L