class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_size = len(height)
        result = 0
        L = 0
        R = height_size - 1

        # Exit the while loop when left/right pointers cross
        # 1. Pick whichever is smaller between height[L] and height[R] as H
        # 2. Calculate W
        # 3. Assign the maximum between result and area(W*H) to result
        while L < R:
            H = 0
            W = R - L

            if height[L] < height[R]:
                H = height[L]
                L += 1
            elif height[L] > height[R]:
                H = height[R]
                R -= 1
            else:
                H = height[L]
                L += 1
                R -= 1
            result = max(result, H * W)
        return result
