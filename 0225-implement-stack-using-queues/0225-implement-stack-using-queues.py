"""
Understanding:
Use two queues(FIFO) to implement a stack(LIFO) with contructor, push, pop, top, and empty

Planning:
Use two queues to implement stack
Time complexity:
push: O(n)
pop: O(1)
top: O(1)
empty: O(n)
Space complexity:
O(n)
"""

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """
        q: 5,10,5,x
        """
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        """
        q: 5,10,5
        return x
        """
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()