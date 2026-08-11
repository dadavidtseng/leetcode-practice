class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> window; // stores char and frequency
        int left = 0;
        int result = 0;
        int maxFrequency = 0;

        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            char const c = s[i];

            // add the frequency of c in window
            window[c]++;

            // update the maxFrequency when window[c] updates
            maxFrequency = max(maxFrequency, window[c]);

            // while window length(i-left+1) minus maxFrequency in window is greater than k,
            // means that this window is invalid
            while ((i - left + 1) - maxFrequency > k) {
                window[s[left]]--; // remove the left char in window
                left++;            // move left pointer to right
            }

            // update the result if window length is greater than previous result
            result = max(result, i - left + 1);
        }

        return result;
    }
};