"""
# Understand
Given an integer array stones, each stone's value might be positive and negative (-10^4 <= stones[i] <= 10^4).
1. In each turn, at least 2 leftmost stones will be removed (x > 1)
2. The sum of removed stones will be added to the left of stones
3. The game stops when there's one stone left, so there's a chance Bob's score is 0 (2 <= n <= 10^5)
4. Alice's goal -> max; Bob's goal -> min
5. Return the score difference between Alice and Bob if they both play optimally.

# Match
Array, Prefix, DP, Game Theory

# Plan
Alice would want to get the positive stones, assuming Bob can always pick at least sum(Alice picks) + (one stone after Alice picks) + more. Both Alice and Bob wants largest sum possible so that they can meet their goals. So we need to find maxDiff.

Alice: sum([0, x])
Bob: sum(sum([0, x]) + sum([x+1, y]))

Since the sum(stones) doesn't change at all, we can build a prefix array from stones
In each turn, the player pick index u and get prefix[u] to the score, where u > 1 because x > 1.
"""
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        stones_size = len(stones)

        # Compute the prefix array.
        # Note that we could create a dedicate prefix array, 
        # but we can just modify stones in this case
        for i in range(1, stones_size):
            stones[i] += stones[i - 1]
        
        # stones[-1] is the sum all original stones
        result = stones[-1]

        # Iterate through (stones_size - 2) to 1
        # Notice that we use (stones_size - 2) 
        # because the stones[stones_size - 1] has already been used by result
        for i in range(stones_size - 2, 0, -1):
            result = max(result, stones[i] - result)
        return result
"""
# Review
To know that Alice's intension is the same as Bob's because of the game rule was hard. And come up with prefix and maxDiff was hard... This kind of problem is always hard to come up with a core idea it's trying to ask, but once you know the core idea, the code is usually not that complicated. Interesting problem overall. 

# Evaluate
stones = (A) + (B) + (C)
prefix = (A) + (A+B) + (A+B+C)
Alice  = (A+B)
Bob    = (A+B+C)
scores = -C, which is essentially prefix[1] - prefix[2]

After walking through the easiest stone game, I was able to understand this problem. But I think the proper way is to come up with a top-down version and then bottom-up optimization.

# Complexity
Time: O(n)
Space: O(1)
"""
