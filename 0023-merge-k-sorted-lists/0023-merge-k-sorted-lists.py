# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        # Iterate through lists and push every list into nodes
        for i in range(len(lists)):
            while lists[i]:
                nodes.append(lists[i].val)
                lists[i] = lists[i].next

        # Sort every node, which creates O(n log n) for time complexity
        nodes.sort()

        result = ListNode(0)
        curr = result

        # Iterate through nodes,
        # 1. Create new node using nodes[i]
        # 2. Advance current node
        for i in range(len(nodes)):
            curr.next = ListNode(nodes[i])
            curr = curr.next

        # Return result's next node because result is a dummy node
        return result.next
