class MyLinkedList:
    class ListNode:
        def __init__(self, val: int = 0, next: ListNode = None):
            self.val: int = val
            self.next: ListNode = next

    def __init__(self):
        # dummy node
        self.head = self.ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        count = 0

        while curr.next:
            if count == index:
                break
            count += 1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_head = self.ListNode(val, self.head.next)
        self.head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        new_tail = self.ListNode(val)
        curr.next = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        curr = self.head
        count = -1

        while curr.next:
            if count == index - 1:
                new_node = self.ListNode(val, curr.next)
                curr.next = new_node
                self.size += 1
                break
            count += 1
            curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return -1
        curr = self.head
        count = -1

        while curr.next:
            if count == index - 1:
                curr.next = curr.next.next
                self.size -= 1
                break
            count += 1
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
