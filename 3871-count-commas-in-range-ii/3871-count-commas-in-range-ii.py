class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        p = 1000
        
        while p <= n:
            result += n - p + 1
            p *= 1000
        return result