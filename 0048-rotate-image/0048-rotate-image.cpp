class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int L = 0;
        int R = static_cast<int>(matrix.size()) - 1;

        while (L < R) {
            for (int i = 0; i < (R - L); ++i) {
                int top = L;
                int bottom = R;

                // Cache the top left
                int topLeft = matrix[top][L + i];

                // Move bottom left to top left
                matrix[top][L + i] = matrix[bottom - i][L];

                // Move bottom right to bottom left
                matrix[bottom - i][L] = matrix[bottom][R - i];

                // Move top right to bottom right
                matrix[bottom][R - i] = matrix[top + i][R];

                // Move top left to top right
                matrix[top + i][R] = topLeft;
            }
            // Move left/right pointers to inner layer
            R--;
            L++;
        }
    }
};