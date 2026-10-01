class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        R = m + n - 1
        i = m - 1
        j = n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[R] = nums1[i]
                i -= 1
            else:
                nums1[R] = nums2[j]
                j -= 1
            R -= 1
        