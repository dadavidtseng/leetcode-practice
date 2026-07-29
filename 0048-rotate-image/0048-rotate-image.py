class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L = 0
        R = len(matrix) - 1

        while L < R:
            for i in range(R - L):
                top = L
                bottom = R

                # Cache the top left
                top_left = matrix[top][L + i]

                # Move bottom left to top left
                matrix[top][L + i] = matrix[bottom - i][L]

                # Move bottom right to bottom left
                matrix[bottom - i][L] = matrix[bottom][R - i]

                # Move top right to bottom right
                matrix[bottom][R - i] = matrix[top + i][R]

                # Move top left to top right
                matrix[top + i][R] = top_left

            # Move left/right pointers to inner layer
            L += 1
            R -= 1
