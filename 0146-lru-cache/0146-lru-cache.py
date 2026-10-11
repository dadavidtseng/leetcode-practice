class LRUCache:
    def __init__(self, capacity: int):
        self.cache = []  # stores [(key, value)]
        self.capacity = capacity

    def get(self, key: int) -> int:
        # Iterate through cache
        # If current cache's key equals key
        # 1. Pop it from the cache list and store it as temp
        # 2. Push temp into cash list
        # 3. Return temp's value
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]

        # Return -1 if key doesn't exist
        return -1

    def put(self, key: int, value: int) -> None:
        n = len(self.cache)

        # Iterate through cache
        # If current cache's key equals key
        # 1. Pop it from the cache list and store it as temp
        # 2. Update temp[1] with value
        # 3. Push temp into cash list
        # 4. Return
        for i in range(n):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                temp[1] = value
                self.cache.append(temp)
                return

        # If key isn't in cache list
        # 1. Remove the oldest cache if the cache is full
        # 2. Push [key, value] into cache
        # Note that we're using [key, value] instead of (key, value)
        # because tuple is immutable
        else:
            if self.capacity == n:
                self.cache.pop(0)
            self.cache.append([key, value])
