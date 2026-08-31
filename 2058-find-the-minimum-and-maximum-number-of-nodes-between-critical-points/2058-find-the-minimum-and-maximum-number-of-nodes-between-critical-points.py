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
        curr_idx = 1
        first_idx = -1
        last_idx = -1

        # Iterate through the linkedlist
        while curr and curr.next:
            if (prev.val > curr.val < curr.next.val) or (
                prev.val < curr.val > curr.next.val
            ):
                if last_idx != -1:
                    min_dist = min(min_dist, curr_idx - last_idx)
                if first_idx == -1:
                    first_idx = curr_idx
                last_idx = curr_idx
            curr_idx += 1
            prev = curr
            curr = curr.next
        return [-1, -1] if first_idx == last_idx else [min_dist, last_idx - first_idx]
