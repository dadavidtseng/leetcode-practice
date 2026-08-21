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
        def lcm(a, b):  # O(1) because 1 <= coins[i] <= 25
            x, y = a, b

            # Calculate greatest common divisor(gcd)
            while y:
                x, y = y, x % y

            # Return least common multiple(lcm),
            # Note that we use a // x * b because (a * b // x)'s (a * b) might overflow
            return a // x * b

        L = min(coins)  # x_min
        R = min(coins) * k  # x_max

        # Precompute all possible subsets in coins
        subsets = []

        # Iterate through every masks
        # Note that we can also use 2 ** len(coins) here
        # because left shift 1 bit means multiply by 2 once.
        for mask in range(1, 1 << len(coins)):  # O(2^n - 1)
            subset_lcm = 1
            subset_size = 0

            # Iterate through every coin
            for i in range(len(coins)):  # O(n)
                # If current coin is selected by current mask
                # 1. Increment subset_size
                # 2. Calculate current subset's lcm
                if mask & (1 << i):
                    subset_size += 1
                    subset_lcm = lcm(subset_lcm, coins[i])

                    # Break if we're outside the range
                    # and there's no need to keep calculating subset_lcm
                    if subset_lcm > R:
                        break
            # After calculating subset_lcm for current mask,
            # if we're still inside the range,
            # push (subset_lcm, sign) into subsets array
            if subset_lcm <= R:
                sign = 1 if subset_size % 2 else -1
                subsets.append((subset_lcm, sign))

        # x is the amount of coins we want to make,
        # return the distinguish amount using every coins.
        # Ex. x=10, coins=[2,5], return= 10//2 + 10//5 - 10//1cm(2,5)
        def count(x: int) -> int:
            result = 0

            for subset_lcm, sign in subsets:  # O(2^n - 1)
                result += sign * (x // subset_lcm)
            return result

        # Perform a binary search to find the exact k we can produce using every coins
        while L < R:  # O(log R) = O(log (min(coins) * k))
            M = L + (R - L) // 2
            if count(M) < k:
                L = M + 1
            else:
                R = M
        return L


"""
# Review
I was able to come up with the naive solution using set and the concept of binary search. It was fun solving and learning this problem, but I don't think I can come up with the solution in an interview without hints because it covers a lot of concepts to solve.

# Evaluate
I guess my focus should be on medium problem and occationally do hard problem. When solving hard problem, it can easily review concepts in wider rages.

# Complexity
Time: O(2^n * (n + log(min(coins) * k)))
Space: O(2^n)
"""
