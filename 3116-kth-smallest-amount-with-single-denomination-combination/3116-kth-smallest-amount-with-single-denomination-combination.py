"""
# Understand
Provided an integer array coins find return the kth smallest amount that can be made using these coins. We can only use one type of these coins. For example, if coins= [3,6,9], x can be made up by only 3 or 6 or 9, which means that x might be 3: 3,6,9,12,15,etc or 6: 6,12,18,24,etc or 9: 9,18,27,36,etc.

# Match
Binary Search

# Plan
As we can see in the example above, the possible x might contain duplicates, such as 12. The naive way would be
```python3[]
def findKthSmallest(self, coins: List[int], k: int) -> int:
        s = set()
        for coin in coins:
            c = coin
            for _ in range(k):
                s.add(coin)
                coin += c
        s=sorted(s)
        return list(s)[k-1]
```
, but this will give us `Memory Limit Exceeded` because k's upper bound is 2 * 10^9.

We could calculate x using k.
For example,
coins= [3,6], if k=3, we know that the smallest possible amount x is `3*1=3` and the largest possible amount of x is 6*3=18. So, when we do `x // coin`, we can get 3 // 3 = 1 and 18 // 3 = 6. At this point, we know that we could perform a binary search for this problem.

Note that,
1. There are duplicates of possible x can be made up by coin
2. The range of x is 3*1 and 3*3 because it's not possible that we use up all 6s, but we could use up all 3s and it could only be less than 3*3.
"""


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a, b):
            x, y = a, b

            while y:
                x, y = y, x % y
            return a // x * b

        L = min(coins)  # x_min
        R = min(coins) * k  # x_max

        subsets = []

        for mask in range(1, 1 << len(coins)):
            subset_lcm = 1
            subset_size = 0

            for i in range(len(coins)):
                if mask & (1 << i):
                    subset_size += 1
                    subset_lcm = lcm(subset_lcm, coins[i])

                    if subset_lcm > R:
                        break
            if subset_lcm <= R:
                sign = 1 if subset_size % 2 else -1
                subsets.append((subset_lcm, sign))

        def count(x: int) -> int:
            result = 0

            for subset_lcm, sign in subsets:
                result += sign * (x // subset_lcm)
            return result

        while L < R:
            M = L + (R - L) // 2
            if count(M) >= k:
                R = M
            else:
                L = M + 1
        return L
