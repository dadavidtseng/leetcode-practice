class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_size = len(matrix)

        # Reverse the matrix horizontally
        matrix.reverse()

        # Transpose the matrix
        for i in range(matrix_size):
            for j in range(i + 1, matrix_size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
