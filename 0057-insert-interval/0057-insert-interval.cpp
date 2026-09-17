class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        // Return newInterval if intervals is empty
        if (intervals.empty()) {
            return {newInterval};
        }

        const int n = static_cast<int>(intervals.size());
        vector<vector<int>> result;

        // Iterate through intervals
        // 1. Completely after newInterval
        // 2. Completely before newInterval
        // 3. Overlapping with newInterval
        for (int i = 0; i < n; ++i) {
            const int currStart = intervals[i][0];
            const int currEnd = intervals[i][1];
            const int newStart = newInterval[0];
            const int newEnd = newInterval[1];

            if (currStart > newEnd) {
                result.push_back(newInterval);
                copy(intervals.begin() + i, intervals.end(),
                     back_inserter(result));
                return result;
            } else if (currEnd < newStart) {
                result.push_back(intervals[i]);
            } else {
                newInterval[0] = min(newStart, currStart);
                newInterval[1] = max(newEnd, currEnd);
            }
        }
        result.push_back(newInterval);
        return result;
    }
};