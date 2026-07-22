class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);

        // Iterate through 1 to n
        for (int i = 1; i <= n; ++i) {
            result[i] = popcount(static_cast<unsigned int>(i));
        }
        return result;
    }
};