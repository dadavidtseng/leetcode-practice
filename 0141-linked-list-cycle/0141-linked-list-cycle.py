# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Exit the while loop if we are
        # 1. At the end of the linked list
        # 2. At one node before the end of the linked list
        while fast and fast.next:
            # Advance slow pointer by one node
            # and fast pointer by two nodes
            slow = slow.next
            fast = fast.next.next

            # Return true if slow equals to fast
            if slow == fast:
                return True

        # Return false if we've reached the end of the linked list
        return False
