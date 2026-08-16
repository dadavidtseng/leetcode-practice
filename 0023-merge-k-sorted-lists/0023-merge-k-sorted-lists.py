# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def conquer(
            listA: Optional[ListNode], listB: Optional[ListNode]
        ) -> Optional[ListNode]:
            # Create a dummy node that points to nothing
            # and attach a tail node on that dummy node
            dummy = ListNode(0, None)
            tail = dummy

            # Exit the while loop when listA and listB are both exhausted
            while listA and listB:
                # If listA's value is smaller than listB's value
                # 1. Attach listA to tail
                # 2. Advance listA
                if listA.val < listB.val:
                    tail.next = listA
                    listA = listA.next
                # If listA's value is larger or equal to listB's value
                # 1. Attach listB to tail
                # 2. Advance listB
                else:
                    tail.next = listB
                    listB = listB.next

                # Advance tail
                tail = tail.next

            # Attach the remaining of listA and listB to tail
            tail.next = listA if listA else listB

            # Return the head of the merged list
            return dummy.next

        def divide(L: int, R: int) -> Optional[ListNode]:
            if L > R:
                return None
            if L == R:
                return lists[L]

            M = L + (R - L) // 2
            left = divide(L, M)
            right = divide(M + 1, R)
            return conquer(left, right)

        # Return empty if lists is empty
        if not lists:
            return None

        # Return divid and conquer using left/right pointers start from the first and last idx
        return divide(0, len(lists) - 1)
