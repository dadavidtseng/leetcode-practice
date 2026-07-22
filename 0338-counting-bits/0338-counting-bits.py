class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        # Iterate through 1 to n
        for num in range(1, n + 1):
            # Iterate through all 32 bits in num
            for i in range(32):
                # Increment result[num] if ith bit in num is 1
                if num & (1 << i):
                    result[num] += 1
        return result