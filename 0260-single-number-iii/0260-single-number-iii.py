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
        # Iterate through nums, perform nums[i]^nums[i-1] to get a^b
        for i in range(len(nums)):
            a_xor_b ^= nums[i]
        nums_a = []
        nums_b = []
        bit = 0
        # (nums[i]>>i) & 1 to know which bit is bit and use this to separate nums into two groups
        for i in range(32):
            if ((a_xor_b>>i) & 1) == 1:
                bit = i
                break

        for i in range(len(nums)):
            if ((nums[i]>>bit) & 1) == 1:
                nums_a.append(nums[i])
            else:
                nums_b.append(nums[i])
        print(f"nums_a={nums_a}, nums_b={nums_b}")
        a = 0
        b = 0
        # Iterate through nums_a and nums_b, perform nums[i]^nums[i-1] again to get a and b from them
        for i in range(len(nums_a)):
            a ^= nums_a[i]
        for i in range(len(nums_b)):
            b ^= nums_b[i]
        return [a, b]
