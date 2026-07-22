class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        offset = 1

        # Iterate through 1 to n
        for num in range(1, n + 1):
            # Update offset to the new highest bit value
            # when num reaches the next power of two
            if offset * 2 == num:
                offset = num

            # offset represents the highest set bit of num
            # Remove that highest bit by subtracting offset from num
            # Reuse the previously computed result of the remaining bits
            result[num] = 1 + result[num - offset]
        return result