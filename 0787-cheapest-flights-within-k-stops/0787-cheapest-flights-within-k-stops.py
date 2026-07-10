class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = [price for price in prices]
            for start, end, cost in flights:
                if prices[start] != float("inf"):
                    temp[end] = min(temp[end], prices[start] + cost)
            prices = temp

        if prices[dst] == float("inf"):
            return -1

        return int(prices[dst])
