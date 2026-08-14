# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Attach a dummy node before head
        # 2. Attach slow pointer to dummy so it's a node before head
        # 3. Attach fast pointer to head
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # Advance fast pointer by n nodes
        while n > 0:
            fast = fast.next
            n -= 1

        # Advance slow/fast pointers and exit the while loop when finished iterating the linkedlist
        while fast:
            slow = slow.next
            fast = fast.next

        # Slow pointer is now a node before the node to remove
        # so this is essentially removing the target node from the linkedlist
        slow.next = slow.next.next

        # Return dummy.next, which is the new head
        # Note that,
        # 1. In head removal case(single node), dummy.next is nullptr
        # 2. We don't return head because head might be the removal target
        return dummy.next
