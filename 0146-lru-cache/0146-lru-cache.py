class Node:
    def __init__(self, key=0, value=0) -> None:
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Create left/right dummy nodes and link them together
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node) -> None:
        # Link node's prev and next together, so that node is removed
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _insert(self, node) -> None:
        # Get one node before right node and right node
        # Insert node between them and link three nodes together in bidirection
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        # If key is in cache
        # 1. Remove this key-value pair
        # 2. Store this key-value pair in one node before right node
        # 3. Return this key-value pair's value
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value

        # Return -1 if key isn't in cache
        return -1

    def put(self, key: int, value: int) -> None:
        # If key is in cache
        # 1. Update this node's value
        # 2. Remove this node from cache
        # 3. Insert this node to one node before right node
        # 4. Return
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert(node)
            return

        # If cache is full
        # 1. Remove lru from the linkedlist
        # 2. Delete lru's key-value pair from cache
        if self.capacity == len(self.cache):
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

        # Create new node and push it into cache
        # Insert that new node as one node before right node
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
