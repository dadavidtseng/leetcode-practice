class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Create a map to store char and index
        unordered_map<char, int> m;
        int L = 0;
        int result = 0;

        // Extend right pointer and store it in the map
        // 1. Move left pointer over right pointer only if we've seen it before
        // 2. Store the index into right pointer's character in the map
        // 3. Update result to keep track of longest window(substring)
        for (int R = 0; R < static_cast<int>(s.size()); ++R) {
            char const c = s[R];

            if (m.contains(c)) {
                L = max(L, m[c] + 1);
            }
            m[c] = R;
            result = max(result, R - L + 1);
        }
        return result;
    }
};