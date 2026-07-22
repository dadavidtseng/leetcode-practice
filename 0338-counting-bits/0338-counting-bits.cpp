class Solution {
public:
    vector<int> countBits(int n) {
       vector<int> result(n + 1, 0);
        int offset = 1;

        // Iterate through 1 to n
        for (int num = 1; num <= n; ++num) {
            // Update offset to the new highest bit value
            // when num reaches the next power of two
            if (offset * 2 == num) {
                offset = num;
            }
            // offset represents the highest set bit of num
            // Remove that highest bit by subtracting offset from num
            // Reuse the previously computed result of the remaining bits
            result[num] = 1 + result[num - offset];
        }
        return result;
    }
};