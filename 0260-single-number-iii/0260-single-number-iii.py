"""
Understand:
Provided an integer array nums that
1. Two elements appear only once
2. All the other elements appear exactly twice(this could be any amount)
3. Return the two elements that appear only once
Required time complexity: O(n), space complexity: O(1)

Match:
Array, Bit Manipulation

Plan:
x^x=0
x^0=x
Iterate through nums, and perform nums[i]^nums[i-1]
We will get a^b, which is what we want to return [a,b]
XOR:
1^0=1
0^1=1
0^0=0
1^1=0
a^b=00001000, this means that on bit 1, it's guarantee that a and b are different
We could separate them into 2 groups, and do the same to other numbers too
Then we can perform nums[i]^nums[i-1] again to get a and b from these two groups
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a_xor_b = 0

        # Iterate through nums
        for i in range(len(nums)):
            # x^x=0
            # x^0=x
            a_xor_b ^= nums[i]

        bit = 0

        # (nums[i]>>i) & 1 to know which bit is either 0 or 1
        for i in range(32):
            if ((a_xor_b >> i) & 1) == 1:
                bit = i
                break

        a = 0
        b = 0

        # Iterate through nums again
        for i in range(len(nums)):
            # If nums[i]'s bit is 1, it belongs to group a,
            # otherwise, it belongs to group b
            if ((nums[i] >> bit) & 1) == 1:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return [a, b]


"""
Review:
When thinking about using bit manipulation to solve any problem, I should write out the
bit itself for thinking about the solution and debugging. It was a little bit tricky to
come up with XOR's feature where XOR=1 means they must have two different bits, thus can be
seperated to two groups, and we could perform the x^x=0, x^0=x again.

Evaluate:
Bit manipulation solution isn't always straight forward. I should practice more bit operation
so that this can become some kind of intuitive that I can come up with solution around it.

Complexity:
Time: O(n)
Space: O(1)
"""
