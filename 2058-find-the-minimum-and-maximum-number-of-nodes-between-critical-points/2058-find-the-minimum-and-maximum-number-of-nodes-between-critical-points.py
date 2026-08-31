# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        def is_critical(x, y, z) -> bool:
            return (y.val - x.val) * (y.val - z.val) > 0

        # Keep track of minimum/maximum distance between two critical points
        min_dist = float("inf")

        prev, curr, next = head, head.next, head.next.next
        curr_idx = 1
        first_idx = -1
        last_idx = -1

        # Iterate through the linkedlist
        while next:
            if is_critical(prev, curr, next):
                if last_idx != -1:
                    min_dist = min(min_dist, curr_idx - last_idx)
                if first_idx == -1:
                    first_idx = curr_idx
                last_idx = curr_idx
            curr_idx += 1
            prev, curr, next = curr, next, next.next

        return [-1, -1] if first_idx == last_idx else [min_dist, last_idx - first_idx]
