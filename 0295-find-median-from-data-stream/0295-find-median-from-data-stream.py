class MedianFinder:

    def __init__(self):
        self.container = []

    def addNum(self, num: int) -> None:
        self.container.append(num)

    def findMedian(self) -> float:
        self.container.sort()
        size = len(self.container)

        if (size & 1) == 1:
            return self.container[size // 2]
        else:
            return (self.container[size // 2] + self.container[size // 2 - 1]) / 2
