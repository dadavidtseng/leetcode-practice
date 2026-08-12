class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_set<char> charSet(s.begin(), s.end());
        int result = 0;

        // For each distinguish character, maintain a sliding window to find out
        // the max result
        for (char c : charSet) {
            // count is count of c inside the window
            // L is the left pointer of the window
            int count = 0;
            int L = 0;

            // Extend the window by moving its right pointer
            // and record the max substringLength as we go
            for (int R = 0; R < static_cast<int>(s.length()); ++R) {
                if (s[R] == c) {
                    count++;
                }

                // Shrink the window by moving its left pointer when that window
                // is invalid Decrement count if we encounter c when shrinking
                // the window
                while ((R - L + 1) - count > k) {
                    if (s[L] == c) {
                        count--;
                    }
                    L++;
                }
                result = max(result, R - L + 1);
            }
        }
        return result;
    }
};