class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_seen = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_seen
            max_seen = max(max_seen, temp)
        return arr
