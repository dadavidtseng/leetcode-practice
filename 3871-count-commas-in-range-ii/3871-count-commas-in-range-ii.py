class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        num = n
        digit = 0
        while num != 0:
            num //= 10
            digit += 1
        
        if digit < 4:
            result = 0
        elif 3 <digit < 7:
            result = n - 999
        elif 6 <digit < 10:
            result = (n - 999999) * 2 + 999000
        elif 9 <digit < 13:
            result = (n - 999999999) * 3 + 999000000 * 2 + 999000
        elif 12 <digit < 16:
            result = (n - 999999999999) * 4 + 999000000000 * 3 + 999000000 * 2 + 999000
        else:
            result = (n - 999999999999) * 4 + 999000000000 * 3 + 999000000 * 2 + 999000 + 1

        return result