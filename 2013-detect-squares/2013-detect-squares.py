class DetectSquares:

    def __init__(self):
        self.freq = {}

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.freq[p] = self.freq.get(p, 0) + 1

    def count(self, point: List[int]) -> int:
        if len(self.freq) < 3:
            return 0
        qx, qy = point
        result = 0

        for (px, py), count in self.freq.items():
            if px != qx or py == qy:
                continue
            side = py - qy
            c1 = (qx + side, qy)
            c2 = (qx + side, py)

            if c1 in self.freq and c2 in self.freq:
                result += count * self.freq[c1] * self.freq[c2]

            c3 = (qx - side, qy)
            c4 = (qx - side, py)

            if c3 in self.freq and c4 in self.freq:
                result += count * self.freq[c3] * self.freq[c4]
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
