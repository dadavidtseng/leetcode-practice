class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Find the end value in intervals
        max_value = max(end for _, end in intervals)

        # Create a mapping to store what the current start's furtherest end is
        # Note that we're using -1 as invalid to avoid [0, 0] case
        m = [-1] * (max_value + 1)
        for start, end in intervals:
            m[start] = max(m[start], end)

        # Keep track of interval start and what's the current end
        curr_start = curr_end = -1
        result = []

        # Iterate/Scan through m
        for i in range(len(m)):
            # If m[i] is valid
            # 1. Assign i to current start if we haven't found one yet
            # 2. Update current end to find the furtherest
            if m[i] != -1:
                if curr_start == -1:
                    curr_start = i
                curr_end = max(curr_end, m[i])
            # If i catches up with current end,
            # 1. Push current start and current end into result
            # 2. Reset current start and current end to -1
            # Note that we won't be able to find any larger end at this point
            # because creating m is kind of like sorting
            if i == curr_end:
                result.append([curr_start, curr_end])
                curr_start = curr_end = -1
        return result
