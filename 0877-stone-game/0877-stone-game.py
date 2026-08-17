"""
Understand:
Provided a piles with even number elements, the sum of the piles is odd
This guarantees that one of Alice and Bob is going to have a greater number of stones.
Ex. [1,2,3,1],
Alice 1, Bob 2, Alice 3, Bob 1 -> Alice 1+3, Bob 2+1 -> Alice wins
              , Alice 1, Bob 3 -> Alice 1+1, Bob 2+3 -> Bob wins
       , Bob 1, Alice 2, Bob 3 -> Alice 1+2, Bob 1+3 -> Bob wins
              , Alice 3, Bob 2 -> Alice 1+3, Bob 1+2 -> Alice wins
Since the problem says that Alice and Bob will always play optimally,
so in this case, whoever starts first will win the game.
Note that we could return true, but let's write out the recursive solution

Match:
Recursion, DP

Plan:
We can maintain a dp that represents Alice's max total using left/right pointers. Alice only picks when the current piles's element is even number.
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Create a dp to store key (L, R) with value of Alice's max total
        dp = {}

        def dfs(L: int, R: int) -> int:
            # Return 0 if left/right pointers cross
            if L > R:
                return 0

            # Return dp[(L, R)] if we've computed it already
            if (L, R) in dp:
                return dp[(L, R)]

            # Create a boolean flag to determine if this is Alice's turn
            is_even = (R - L) % 2 == 0

            # Alice can only pick when it's her turn
            left = piles[L] if is_even else 0
            right = piles[R] if is_even else 0

            # When unwinding, we want the maximum of Alice picking left/right pointers from the piles
            dp[(L, R)] = max(dfs(L + 1, R) + left, dfs(L, R - 1) + right)
            return dp[(L, R)]

        # Return true if Alice wins, return false otherwise
        total = sum(piles)
        alice = dfs(0, len(piles) - 1)
        return alice > total - alice


"""
Review:
I was able to draw the decision tree, which made this problem easier to understand. However, it's a little bit tricky to know that whoever picks first will always win the game. I think this problem is a problem to study deeply.

Evaluate:
It seems like a common pattern that we can optimize recursive call to DP, which is something I think I should practice more among the harder problems since they're not always intuitive.

Complexity:
Time: O(n^2)
Space: O(n^2)
"""
