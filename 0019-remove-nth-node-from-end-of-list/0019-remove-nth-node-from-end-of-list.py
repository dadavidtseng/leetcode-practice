# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create an empty container to store node
        # and attach head to curr
        nodes = []
        curr = head

        # Push every nodes into container by going through the linkedlist
        while curr:
            nodes.append(curr)
            curr = curr.next

        remove_idx = len(nodes) - n

        # Return early without doing the removal
        if remove_idx == 0:
            return head.next

        # Remove the target node from the linkedlist
        nodes[remove_idx - 1].next = nodes[remove_idx].next

        # Return the modified linkedlist's head
        return head
