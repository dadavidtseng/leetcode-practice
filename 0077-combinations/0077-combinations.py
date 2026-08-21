class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def gosper_hack(mask):
            c = mask & -mask
            r = mask + c
            return (((r ^ mask) >> 2) // c) | r

        mask = (1 << k) - 1
        limit = 1 << n

        while mask < limit:
            comb = []

            for bit in range(n):
                if mask & (1 << bit):
                    comb.append(bit + 1)

            res.append(comb)

            mask = gosper_hack(mask)

        return res
