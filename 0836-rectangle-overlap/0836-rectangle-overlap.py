class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # [x1, y1, x2, y2]
        # bottom-left  [0][1]
        # bottom-right [2][1]
        # top-left     [0][3]
        # top-right    [2][3]
        return (
            rec1[2] > rec2[0]
            and rec2[2] > rec1[0]
            and rec1[3] > rec2[1]
            and rec2[3] > rec1[1]
        )
