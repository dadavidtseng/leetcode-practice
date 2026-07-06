class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) != 0 and num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            top = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top)

    def findMedian(self) -> float:
        result = 0.0

        if len(self.max_heap) > len(self.min_heap):
            result = -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            result = self.min_heap[0]
        else:
            result = (-self.max_heap[0] + self.min_heap[0]) * 0.5
        return result


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
