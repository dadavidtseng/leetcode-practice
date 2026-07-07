class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def digit_square_sum(n: int):
            return sum(int(digit) ** 2 for digit in str(n))

        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)

        return n == 1
