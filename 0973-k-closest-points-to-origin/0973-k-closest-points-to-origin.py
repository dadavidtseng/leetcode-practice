class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist_square(x):
            return x[0] ** 2 + x[1] ** 2

        def partition(L: int, R: int) -> int:
            pivot_idx = R
            pivot_dist_square = dist_square(points[pivot_idx])
            i = L

            # Iterate from L to pivot_idx - 1 (R - 1)
            # If dist_sqaure for points[j] is less than or equal to pivot_dist_square,
            # 1. Swap points[i] and points[j]
            # 2. Increment i by 1
            for j in range(L, pivot_idx):
                if dist_square(points[j]) <= pivot_dist_square:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            # Swap points[i] and points[pivot_idx] and return i, which is the new pivot
            # Every point before pivot is what we want and everything after pivot isn't
            points[i], points[pivot_idx] = points[pivot_idx], points[i]
            return i

        L, R = 0, len(points) - 1

        # This handles the edge case of len(points) == k
        # If pivot = -1, the partition can never return an index equal to len(points)
        pivot = len(points)

        # Exit the while loop when pivot == k because only in this condition we can return points[:k]
        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
