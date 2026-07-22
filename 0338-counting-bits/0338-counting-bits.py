class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        # Iterate through 1 to n
        for i in range(1, n + 1):
            result[i] = i.bit_count()
        return result