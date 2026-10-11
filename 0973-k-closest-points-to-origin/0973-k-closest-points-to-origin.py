class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist_square(x):
            return x[0] ** 2 + x[1] ** 2

        def partition(L: int, R: int) -> int:
            pivot_idx = R
            pivot_dist_square = dist_square(points[pivot_idx])
            i = L

            # Iterate from L to pivot_idx - 1 (R - 1)
            # If dist_sqaure for points[j] is greater than pivot_dist_square,
            # 1. Swap points[i] and points[j]
            # 2. Increment i by 1
            for j in range(L, R):
                if dist_square(points[j]) <= pivot_dist_square:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[R] = points[R], points[i]
            return i

        L, R = 0, len(points) - 1

        if k >= len(points):
            return points

        while True:
            pivot = partition(L, R)
            if pivot == k:
                break
            elif pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
