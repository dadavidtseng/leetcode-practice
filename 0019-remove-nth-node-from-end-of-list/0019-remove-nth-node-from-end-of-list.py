# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_size = 0
        curr = head

        # Calculate the number of nodes in the linkedlist by iterating through it
        while curr:
            nodes_size += 1
            curr = curr.next
        remove_idx = nodes_size - n

        # Return early without doing the removal
        if remove_idx == 0:
            return head.next

        # Move current node back to head for next iteration
        curr = head

        # Iterate through the linkedlist again and break after removing the target node
        for i in range(nodes_size):
            if (i + 1) == remove_idx:
                curr.next = curr.next.next
                break
            curr = curr.next

        # Return the modified linkedlist's head
        return head
