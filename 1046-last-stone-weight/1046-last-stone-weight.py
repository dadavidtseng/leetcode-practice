class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)

            if a != b:
                heapq.heappush(max_heap, -(a - b))

        max_heap.append(0)

        return -max_heap[0]
