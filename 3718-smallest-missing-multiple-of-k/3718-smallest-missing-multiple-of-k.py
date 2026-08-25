"""
Understand
Given a integer array nums and integer k, with 1 <= nums[i] <= 100 and 1 <= k <= 100.
Return the smallest multiple of k based on nums.
Ex. nums= [8,2,3,4,6], k = 2
k's multiple= 2, 4, 6, 8, 10; return 10 because it's not in nums.

Match
Array, Bit Manipulation

Plan
nums[i] // k is the multiplier, if we use these multiplier to set 00000000 with the position, we could eventaully find their smallest missing multiplier.
Ex. nums= [8,2,3,4,6], k = 2, multiplier= [4,1,1.5,2,3], x= 00001111 because only 1,2,3,4 is valid multipler and we set them in x, which was originally 00000000. Then we just have to find the first 0's bit position from x.
"""


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x = 0

        # Iterate through nums
        for num in nums:
            # If num is valid multipler of k
            # Note that we could write if not num % k
            if num % k == 0:
                # 0 <= mask <= 99
                mask = (num // k) - 1

                # 0 | 1 = 1
                # Set multiplier's bit position to 1 in x
                x |= 1 << mask

        result = 0

        # 0 & 1 = 0, 1 & 1 = 1
        # Exit the while loop when finding the lowest 0 in x
        # Note that we could write while (x & (1 << result)) != 0
        while x & (1 << result):
            result += 1

        # result is 0-index, but bit is 1-index
        # so we increment result by 1
        return (result + 1) * k


"""
Review
I was able to solve it quickly using set, but then I found out this bit manipulation solution interesting. Transforming from problem statement to bit manipulation is often hard, but once I got the idea, it was easy and optimized!

Evaluate
Often time we could use bit manipulation to optimize a simple solution. Though, the tradeoff is the readability, so make sure you add comments in the code.

Complexity
Time: O(n)
Space: O(1)
"""
