# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(
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

        # Return empty if lists is empty
        if not lists:
            return None

        # Iterate through lists from index 1 and merge them one by one
        for i in range(1, len(lists)):
            lists[i] = merge_two_lists(lists[i], lists[i - 1])
        return lists[-1]
