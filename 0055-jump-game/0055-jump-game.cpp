class Solution {
public:
    bool canJump(vector<int>& nums) {
        const int size = static_cast<int>(nums.size());

        vector<bool> dp(size, false);
        dp[size - 1] = true;

        // Iterate backwards from an index before the final index to 0,
        // one step at a time
        for (int i = size - 2; i >= 0; --i) {
            // Calculate the maximum index we can reach from current index
            const int end = min(size - 1, i + nums[i]);

            // Iterate forward to see if we can reach any indexes;
            // As soon as we find out that we can reach this index,
            // mark dp[i] to true and break so that we don't do redundant work
            for (int j = i + 1; j <= end; ++j) {
                if (dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }

        // Return true if we've reached the first index
        return dp[0];
    }
};