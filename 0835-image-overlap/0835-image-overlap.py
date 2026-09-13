class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        result = 0
        n = len(img2)

        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):
                overlap = 0
                for row in range(n):
                    for col in range(n):
                        new_row = row + dx
                        new_col = col + dy

                        if (
                            0 <= new_row < n
                            and 0 <= new_col < n
                            and img1[new_row][new_col] * img2[row][col]
                        ):
                            overlap += 1
                result = max(result, overlap)
        return result
