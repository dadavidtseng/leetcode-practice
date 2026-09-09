class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = sum(int(x) for c in s for x in str(ord(c) - ord("a") + 1))

        for _ in range(k - 1):
            num = sum(int(x) for x in str(num))
        return num
