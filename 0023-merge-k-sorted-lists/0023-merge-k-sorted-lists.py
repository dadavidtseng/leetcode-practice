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

        lists_size = len(lists)

        # Return empty if lists is empty
        if lists_size == 0:
            return None

        # Exit the while loop when there's only one list left,
        # which means that everything has been merged
        while lists_size > 1:
            # Reset newSize after a merge
            new_size = 0

            # Iterate lists with 2 steps
            for i in range(0, lists_size, 2):
                # In odd lists case, we should store the last list back to lists
                if (i + 1) == lists_size:
                    lists[new_size] = lists[i]

                # Merge two lists and store back to lists[newSize]
                else:
                    lists[new_size] = merge_two_lists(lists[i], lists[i + 1])

                # Calculate newSize so lists will be shrunk after every operation
                new_size += 1

            # Update listsSize with newSize
            lists_size = new_size

        # Return lists because listsSize is 1 after merging everything
        return lists[0]
