class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freq; // stores char and frequency
        int L = 0;
        int maxFreq = 0;
        int result = 0;

        // Extend the window by moving its right pointer
        // and record the max window size (R-L+1) as we go
        for (int R = 0; R < static_cast<int>(s.length()); ++R) {
            const char c = s[R];

            // Use a frequency map to keep track of the maxFreq for each
            // distinguish character Note that maxFreq may sometimes be
            // inaccurate because we don't decrement it We don't decrement
            // maxFreq because we want to get the maximum window size
            freq[c]++;
            maxFreq = max(maxFreq, freq[c]);

            // Remove the leftmost character from the frequency map as we shrink
            // the window
            while ((R - L + 1) - maxFreq > k) {
                freq[s[L]]--;
                L++;
            }
            result = max(result, R - L + 1);
        }
        return result;
    }
};