class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        min_odd = float("inf")
        min_even = float("inf")

        # Iterate through nums to compute min_odd and min_even
        for n in nums:
            # odd
            if n % 2:
                min_odd = min(min_odd, n)
            # even
            else:
                min_even = min(min_even, n)

        can_odd = True
        can_even = True
        print(min_odd, min_even)
        # Try all odd
        for n in nums:
            if not n % 2:
                if n - min_odd < 1:
                    print("Try all odd")
                    can_odd = False
                    break

        # Try all even
        for n in nums:
            if n % 2:
                if n - min_odd < 1:
                    print("Try all even")
                    can_even = False
                    break
        print(can_odd, can_even)
        return can_odd or can_even
            
