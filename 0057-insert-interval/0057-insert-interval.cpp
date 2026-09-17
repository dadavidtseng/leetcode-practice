class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        // Return newInterval if intervals is empty
        if (intervals.empty()) {
            return {newInterval};
        }

        const int n = static_cast<int>(intervals.size());
        int i = 0;
        vector<vector<int>> result;

        // Intervals completely before newInterval
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            ++i;
        }

        // Intervals that overlap with newInterval
        // 1. new start = minimum of starts
        // 2. new end = maximum of ends
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            ++i;
        }
        result.push_back(newInterval);

        // Intervals completely after the merged newInterval
        while (i < n) {
            result.push_back(intervals[i]);
            ++i;
        }
        return result;
    }
};