class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        # Iterate through 1 to n
        for num in range(1, n + 1):
            # Find previous result by shifting num right by 1, and check if that lowest bit is 1
            result[num] = result[num >> 1] + (num & 1)
        return result
