class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int matrix_size = static_cast<int>(matrix.size());
        vector<vector<int>> rotated(matrix_size, vector<int>(matrix_size, 0));

        for (int i = 0; i < matrix_size; ++i) {
            for (int j = 0; j < matrix_size; ++j) {
                // 1. m[i][j] = m[j][i] -> transpose
                // 2. m[j][(n - 1) - i] -> mirror by x-axis
                rotated[j][(matrix_size - 1) - i] = matrix[i][j];
            }
        }
        matrix = rotated;
    }
};