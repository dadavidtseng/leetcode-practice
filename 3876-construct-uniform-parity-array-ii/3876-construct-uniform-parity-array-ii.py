class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        min_odd = float("inf")
        
        # Iterate through nums to compute min_odd
        for n in nums:
            if n % 2:
                min_odd = min(min_odd, n)

        # All even
        if min_odd == float("inf"):
            return True      
        
        # Try all odd
        for n in nums:
            # even
            if not n % 2 and n - min_odd < 1:
                return False

        return True
            
