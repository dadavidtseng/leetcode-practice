class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        # Iterate through 1 to n
        for i in range(1, n + 1):
            num = i

            # Exit the while loop when n isn't 0
            while num != 0:
                # Flip the rightmost 1 bit to 0
                # Note that n | (n + 1) can flip the rightmost 0 bit to 1
                num = num & (num - 1)
                result[i] += 1
        return result
