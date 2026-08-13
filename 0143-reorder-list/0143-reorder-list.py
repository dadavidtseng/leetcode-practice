# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Return early if provided head is empty or there's only one node in the linkedlist
        if head is None or head.next is None:
            return

        # Note that we could use front = [head] so that we don't need nonlocal front
        # but then we will have tons of front[0] and front[0].next, which is hard to read
        front = head

        def dfs(back) -> bool:
            nonlocal front

            # Return true if back is empty
            if back is None:
                return True

            if not dfs(back.next):
                # Note that this could return whatever because it's just for existing the DFS call
                return False

            # Set the new tail (back->next) to empty and return false
            if front == back or front.next == back:
                back.next = None
                return False

            # Reorder nodes using front/back pointers
            temp = front.next
            front.next = back
            back.next = temp
            front = temp

            return True

        dfs(head.next)
