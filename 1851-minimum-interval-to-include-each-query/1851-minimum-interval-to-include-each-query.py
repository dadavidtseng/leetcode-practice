class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        result = [-1] * len(queries)
        min_heap = []
        idx = 0

        for original_idx, query in sorted_queries:
            while idx < len(intervals) and intervals[idx][0] <= query:
                s, e = intervals[idx]
                heapq.heappush(min_heap, (e - s + 1, e))
                idx += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            if min_heap:
                result[original_idx] = min_heap[0][0]
        return result
