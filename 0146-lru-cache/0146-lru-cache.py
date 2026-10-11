class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # If key is in cache
        # 1. Move this key-value pair to the end of the cache
        # 2. Return this keu-value pair's value
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        # Return -1 if key isn't in cache
        return -1

    def put(self, key: int, value: int) -> None:
        # If key is in cache
        # 1. Move this key-value pair to the end of the cache
        # 2. Update this key-value pair's value
        # 3. Return
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            return

        # Remove lru from it if cache is full
        # Push this new key-value pair in cache
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
