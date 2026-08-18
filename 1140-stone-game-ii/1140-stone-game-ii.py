class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(is_alice: bool, i: int, M: int) -> int:
            piles_size = len(piles)
            if i == piles_size:
                return 0
            if (is_alice, i, M) in dp:
                return dp[(is_alice, i, M)]

            result = 0 if is_alice else float("inf")
            total = 0

            for X in range(1, 2 * M + 1):
                if X + i > len(piles):
                    break
                total += piles[X + i - 1]
                if is_alice:
                    result = max(result, total + dfs(not is_alice, X + i, max(M, X)))
                else:
                    result = min(result, dfs(not is_alice, X + i, max(M, X)))
            dp[(is_alice, i, M)] = result
            return result

        return dfs(True, 0, 1)
