# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Return early if provided head is empty or there's only one node in the linkedlist
        if head is None or head.next is None:
            return

        # Create an empty container to store ListNode*
        # and attach head to curr
        nodes = []
        curr = head

        # Push every nodes into container by going through the linkedlist
        while curr:
            nodes.append(curr)
            curr = curr.next

        L = 0
        R = len(nodes) - 1

        # Reorder nodes using left/right pointers
        while L < R:
            nodes[L].next = nodes[R]
            L += 1
            nodes[R].next = nodes[L]
            R -= 1

        # Set the tail's next pointer points to prevent a cycle
        nodes[L].next = None
