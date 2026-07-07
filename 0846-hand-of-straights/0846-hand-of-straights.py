class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        freq = {}

        for h in hand:
            freq[h] = freq.get(h, 0) + 1

        for h in hand:
            if freq[h] == 0:
                continue

            for i in range(groupSize):
                curr = h + i

                if freq.get(curr, 0) == 0:
                    return False
                freq[curr] -= 1

        return True
