"""
Understand
Given a string num, which contains digital number "0-9" and "?"
1. Each turn, Alice and Bob can replace "?" with "0-9"
2. first != second -> Alice wins, Bob loses; vice versa
3. After replacing all "?", return true if Alice wins, false if Bob wins
4. Alice starts first

Match
Array, String, Greedy, Game Theory

Plan
Depends on how many "?" in num, whoever plays last can win the game
For odd number, Alice wins; for even number, Bob wins
Iterate through num and count "?" to decide who wins

There are some cases we have to consider:
1. no "?" -> compare left and right directly
2. odd "?" -> Alice control last digit -> Alice wins because Bob has no way to respond to Alice
3. even "?" -> Bob control last digit -> check if after Bob responses to Alice, diff is 0
"""

class Solution:
    def sumGame(self, num: str) -> bool:
        num_size = len(num)
        sumL = 0
        sumR = 0
        qL = 0
        qR = 0

        # Compute sumL, sumR, qL, qR
        for i in range(num_size):
            if i < num_size // 2:
                if num[i] == "?":
                    qL += 1
                else:
                    sumL += int(num[i])
            else:
                if num[i] == "?":
                    qR += 1
                else:
                    sumR += int(num[i])

        # Case 1: no "?"
        if qL + qR == 0:
            return sumL != sumR

        # Case 2: odd "?"
        if (qL + qR) % 2 == 1:
            return True

        # Case 3a: even "?" on both sides
        if qL == qR:
            return sumL != sumR

        # Case 3b: even "?" in total, (qL-qR) is odd
        return 2 * (sumL - sumR) != 9 * (qR - qL)

"""
Review
I was able to come up with an idea that whoever controls the last digit wins and I thought about maybe we need to conside which side is "?" at. The core concept of this problem is "who can control the result wins", but for Bob, even if he can control the result, he might still lose. In order for Bob to control the final result, not only does the "?" have to be even number, but he needs to use (9-x) when Alice uses x. That's why we have `2 * (sumL - sumR) != 9 * (qR - qL)`.

Evaluate
Drawing out the round manually helped me to understand this problem better and I think the mental model for the problem needs careful observation. Overall, it was a nice problem!

Complexity
Time: O(n)
Space: O(1)
"""
