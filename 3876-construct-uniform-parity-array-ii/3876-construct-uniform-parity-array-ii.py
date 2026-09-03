class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        # Return true if there's only one element in nums
        if len(nums) == 1:
            return True

        min_odd = float("inf")

        # Iterate through nums to compute min_odd
        for n in nums:
            if n % 2:
                min_odd = min(min_odd, n)

        # odd  + odd  = even
        # odd  + even = odd
        # even + even = even

        # Return true if all elements are even
        if min_odd == float("inf"):
            return True

        # Iterate through nums to find even and see if we can turn it into odd
        for n in nums:
            if not n % 2 and n - min_odd < 1:
                return False
        return True
