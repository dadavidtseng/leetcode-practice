class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        // Return newInterval if intervals is empty
        if (intervals.empty()) {
            return {newInterval};
        }

        const int n = static_cast<int>(intervals.size());
        const int target = newInterval[0];
        int L = 0;
        int R = n - 1;
        vector<vector<int>> result;

        // Use binary search to find the correct position where newInterval
        // should be inserted based on its start time.
        while (L <= R) {
            int M = L + (R - L) / 2;

            if (intervals[M][0] < target) {
                L = M + 1;
            } else {
                R = M - 1;
            }
        }

        // Insert newInterval into intervals at the position of L
        // Noted that after inserting, the list is still sorted by start time.
        intervals.insert(intervals.begin() + L, newInterval);

        // Iterate through intervals
        // If the current interval does not overlap the last interval in the
        // result, append it otherwise merge them by extending the end
        for (const auto& interval : intervals) {
            if (result.empty() || result.back()[1] < interval[0]) {
                result.push_back(interval);
            } else {
                result.back()[1] = max(result.back()[1], interval[1]);
            }
        }
        return result;
    }
};