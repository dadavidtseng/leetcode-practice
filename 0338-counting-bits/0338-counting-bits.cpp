class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);

        // Iterate through 1 to n
        for (int i = 1; i <= n; ++i) {
            int num = i;

            // Exit the while loop when n isn't 0
            while (num != 0) {
                // Flip the rightmost 1 bit to 0
                // Note that n | (n + 1) can flip the rightmost 0 bit to 1
                num = num & (num - 1);
                result[i]++;
            }
        }
        return result;
    }
};