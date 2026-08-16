# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy

        while True:
            # minIdx for picking out the list with smallest node value
            # Note that -1 means nothing has been picked yet
            min_idx = -1

            # Iterate through lists
            for i in range(len(lists)):
                # Continue if lists[i] is empty
                if not lists[i]:
                    continue

                # If we haven't picked anything or
                # if current node's value is smaller than what node we've picked's value,
                # set minIdx to current idx, which means picking that node
                if min_idx == -1 or lists[i].val < lists[min_idx].val:
                    min_idx = i

            # Break out of the while loop if we have nothing to pick
            if min_idx == -1:
                break

            # 1. Attach the picked node to current node
            # 2. Advance current node
            # 3. Advance the list that has been picked for next iteration
            curr.next = lists[min_idx]
            curr = curr.next
            lists[min_idx] = lists[min_idx].next
        return dummy.next
