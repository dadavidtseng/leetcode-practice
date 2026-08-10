class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int L = 0;
        int result = 0;

        // Extend right pointer if we haven't seen that character before
        for (int R = 0; R < static_cast<int>(s.size()); ++R) {
            // Move left pointer until charSet doesn't contain s[R]
            while (charSet.contains(s[R])) {
                charSet.erase(s[L]);
                L++;
            }
            charSet.insert(s[R]);
            result = max(result, R - L + 1);
        }
        return result;
    }
};