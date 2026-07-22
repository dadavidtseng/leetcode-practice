class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);

        // Iterate through 1 to n
        for (int num = 1; num <= n; ++num) {
            // Iterate through all 32 bits in num
            for (int i = 0; i < 32; i++) {
                // Increment result[num] if ith bit in num is 1
                if (num & (1 << i)) {
                    result[num]++;
                }
            }
        }
        return result;
    }
};