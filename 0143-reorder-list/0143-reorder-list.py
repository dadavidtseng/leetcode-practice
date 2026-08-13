# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Return early if provided head is empty or there's only one node in the linkedlist
        if not head or not head.next:
            return

        # Find the middle node in linkedlist using slow/fast pointers
        slow = head
        fast = head

        # Advance slow/fast pointers when
        # 1. Fast pointer is not nullptr(even list)
        # 2. Fast pointer's next is not nullptr(odd list)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list in half
        # 1. Attach original head to first
        # 2. Attach slow pointer's next to second(this works both on odd/even list)
        # 3. Cut the second half from first half(original head)
        first = head
        second = slow.next
        slow.next = None

        # Reverse the second list
        # 1. Store the next node in temp
        # 2. Set the next node to prev
        # 3. Advance the prev node
        # 4. Advance the curr node
        # Attach prev to the head of second half(cur is nullptr now)
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev

        # Iterate through the first haft and insert the second half one after another in first half
        # exit the loop when second is empty
        #
        # Note that we don't need to check first because for first half is one node more than second
        # half in odd list
        while second:
            temp_first = first.next
            temp_second = second.next

            # Reorder nodes
            first.next = second
            second.next = temp_first

            # Advance first and second for next iteration
            first = temp_first
            second = temp_second
