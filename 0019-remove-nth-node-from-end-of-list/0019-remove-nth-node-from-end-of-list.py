# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(head):
            nonlocal n

            # Return empty if we've reached the end of the linkedlist
            if not head:
                return None

            # The shape of the DFS call is
            # DFS(head){head's next}, so it's iterating through the linkedlist
            head.next = dfs(head.next)

            # n was passed in by reference in order to really modify it in DFS call
            n -= 1

            # Return this node's next node so that it can be linked with this node's previous node,
            # which is essentially removing this node from the linked list
            if n == 0:
                return head.next

            # Return head, which was passed in this DFS call
            # so that the unwinding process won't modify anything in the linkedlist
            return head

        return dfs(head)
