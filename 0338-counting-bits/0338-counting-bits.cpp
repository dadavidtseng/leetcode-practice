class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);

        // Iterate through 1 to n
        for (int num = 1; num <= n; ++num) {
            // Find previous result by shifting num right by 1, and check if
            // that lowest bit is 1
            result[num] = result[num >> 1] + (num & 1);
        }
        return result;
    }
};