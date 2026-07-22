class Solution {
public:
    int maxArea(vector<int>& height) {
        const int heightSize = static_cast<int>(height.size());
        int result = 0;
        int L = 0;
        int R = heightSize - 1;

        // Exit the while loop when left/right pointers cross
        // 1. Pick whichever is smaller between height[L] and height[R] as H
        // 2. Calculate W
        // 3. Assign the maximum between result and area(W*H) to result
        while (L < R) {
            int H = 0;
            const int W = R - L;

            if (height[L] < height[R]) {
                H = height[L];
                L++;
            } else if (height[L] > height[R]) {
                H = height[R];
                R--;
            } else {
                H = height[L];
                L++;
                R--;
            }
            result = max(result, H * W);
        }
        return result;
    }
};