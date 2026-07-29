class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_size = len(matrix)
        rotated = [[0] * matrix_size for _ in range(matrix_size)]

        for i in range(matrix_size):
            for j in range(matrix_size):
                # 1. m[i][j] = m[j][i] -> transpose
                # 2. m[j][(n - 1) - i] -> mirror by x-axis
                rotated[j][(matrix_size - 1) - i] = matrix[i][j]
        matrix[:] = rotated