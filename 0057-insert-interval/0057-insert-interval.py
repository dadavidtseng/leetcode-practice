class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # Return newInterval if intervals is empty
        if not intervals:
            return [newInterval]

        n = len(intervals)
        result = []

        # Iterate through intervals
        # 1. Completely after newInterval
        # 2. Completely before newInterval
        # 3. Overlapping with newInterval
        for i in range(n):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            new_start = newInterval[0]
            new_end = newInterval[1]

            if curr_start > new_end:
                result.append(newInterval)
                return result + intervals[i:]
            elif curr_end < new_start:
                result.append(intervals[i])
            else:
                newInterval = [min(new_start, curr_start), max(new_end, curr_end)]
        result.append(newInterval)
        return result
