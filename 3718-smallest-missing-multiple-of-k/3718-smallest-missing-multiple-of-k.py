class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set()

        for num in nums:
            s.add(num)

        for i in range(1, 102):
            if i * k not in s:
                return i * k
