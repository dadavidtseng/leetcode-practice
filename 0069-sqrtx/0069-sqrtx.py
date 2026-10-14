class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        L, R = 0, x // 2
        while L <= R:
            M = L + (R - L) // 2
            if M * M == x:
                return M
            elif M * M < x:
                L = M + 1
            else:
                R = M - 1
        return R
