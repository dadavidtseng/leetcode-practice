class Solution {
public:
    bool canJump(vector<int>& nums) {
        const int size = static_cast<int>(nums.size());

        // Create memo with nums' size and set them all to 0(unknown)
        // memo[size-1] marks the final success state for dfs call's base case
        // 0 = unknown, 1 = good, -1 = bad
        vector<int> memo(size, 0);
        memo[size - 1] = 1;
        return dfs(nums, memo, 0);
    }

private:
    static bool dfs(vector<int>& nums, vector<int>& memo, int i) {
        // If this index has been visited,
        // return true if we can reach it
        if (memo[i] != 0) {
            return memo[i] == 1;
        }

        // Calculate the maximum index we can reach from current index
        int end = min((int)nums.size() - 1, i + nums[i]);

        // Iterate through all possible index,
        // return true and mark in memo if we can reach any of them
        // Note that the recursive call and next = pos + 1 is like testing every
        // possibilities as we step further, but memo allows us not to step
        // twice
        for (int next = i + 1; next <= end; ++next) {
            if (dfs(nums, memo, next)) {
                memo[i] = 1;
                return true;
            }
        }

        // Mark in memo that we can't reach this position and return false
        memo[i] = -1;
        return false;
    }
};
