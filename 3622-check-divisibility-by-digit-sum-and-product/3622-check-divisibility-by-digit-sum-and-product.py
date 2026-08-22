"""
Understand
Given a integer n with a range of 1 <= n <= 10^6,
return true if n is divisible by the sum of,
1. digit sum of n
2. digit product of n

Match
Math

Plan
Extract n's digit and compute the sum and product of the digit
return true if n % (sum + product) == 0
"""


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        total = 0
        product = 1

        # Use a while loop
        while n:
            # n % 10 to extract the last digit
            digit = n % 10

            # n // 10 to remove the last digit
            n //= 10

            # Compute the sum and product of all digits
            total += digit
            product *= digit

        # Return true if n % (sum + product) == 0
        return num % (total + product) == 0


"""
Review
The core concept of this solution is integer manipulation using `%` and `//`

Evaluate
There are also other ways to do this question, such as string conversion and mapping from string to integer.

Complexity:
Time: O(log10(n)), the value of n scales by a factor of 10 for each digit added.
Space: O(1)
"""
