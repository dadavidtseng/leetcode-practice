class Solution:
    def countCommas(self, n: int) -> int:
        return 0 if n <= 999 else n - 1000 + 1