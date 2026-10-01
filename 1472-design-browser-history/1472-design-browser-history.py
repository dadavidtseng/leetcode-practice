class BrowserHistory:
    class ListNode:
        def __init__(self, val: str = "", prev: ListNode = None, next: ListNode = None):
            self.val: str = val
            self.prev: ListNode = prev
            self.next: ListNode = next

    def __init__(self, homepage: str):
        self.curr = self.ListNode(homepage)

    def visit(self, url: str) -> None:
        new_tail = self.ListNode(url)
        self.curr.next = new_tail
        new_tail.prev = self.curr
        self.curr = new_tail

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
