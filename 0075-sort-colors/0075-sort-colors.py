class Solution:
    def sortColors(self, nums: list[int]) -> None:
        freq = [0] * 3

        for num in nums:
            freq[num] += 1

        i = 0
        for n in range(3):
            for j in range(freq[n]):
                nums[i] = n
                i += 1
