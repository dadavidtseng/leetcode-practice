class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int matrix_size = static_cast<int>(matrix.size());

        // Reverse the matrix horizontally
        reverse(matrix.begin(), matrix.end());

        // Transpose the matrix
        for (int i = 0; i < matrix_size; ++i) {
            for (int j = i + 1; j < matrix_size; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};