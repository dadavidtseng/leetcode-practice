# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]

        # Keep track of minimum/maximum distance between two critical points
        min_dist = float("inf")

        curr = head
        prev = curr
        curr = curr.next
        prev_idx = 0
        curr_idx = 1
        first_idx = -1

        # Iterate through the linkedlist
        while curr and curr.next:
            

            if (prev.val > curr.val and curr.next.val > curr.val) or (prev.val < curr.val and curr.next.val < curr.val):
                if prev_idx != 0:
                    min_dist = min(min_dist, curr_idx - prev_idx)
                prev_idx = curr_idx
                if first_idx == -1:
                    first_idx = curr_idx
            print(min_dist, curr_idx, prev_idx)

            curr_idx += 1
            prev = curr
            curr = curr.next

        if first_idx == -1 or prev_idx == first_idx:
            return [-1,-1]

        return [min_dist, prev_idx - first_idx]
