class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}

        for idx, c in enumerate(s):
            last_idx[c] = idx

        result = []
        size = 0
        end = 0

        for idx, c in enumerate(s):
            size += 1
            end = max(end, last_idx[c])

            if idx == end:
                result.append(size)
                size = 0
        return result
