# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Return empty if lists is empty
        if not lists:
            return None

        counter = 0
        min_heap = []

        # Iterate through lists
        for i in range(len(lists)):
            # Push lists[i] into min heap if it's not empty
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, counter, lists[i]))
                counter += 1

        result = ListNode(0, None)
        curr = result

        # Exit the while loop when min heap is empty
        while min_heap:
            # Pop a node from min heap, it'll be the smallest node
            _, _, node = heapq.heappop(min_heap)

            # 1. Attach the node to current node
            # 2. Advance current node
            # 3. Advance the node for next iteration
            # 4. If node is not empty, push it into min heap
            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1

        # Return result's next node because result is a dummy node
        return result.next
