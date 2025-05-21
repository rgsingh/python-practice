
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}       # key → value
        self.usage = []       # track access order: least recent → most recent

    def get(self, key):
        if key not in self.cache:
            return -1
        # Update usage
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update value and usage
            self.cache[key] = value
            self.usage.remove(key)
            self.usage.append(key)
        else:
            # Evict if at capacity
            if len(self.cache) >= self.capacity:
                lru = self.usage.pop(0)
                del self.cache[lru]
            self.cache[key] = value
            self.usage.append(key)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 1
    cache.put(3, 3)       # Evicts key 2
    print(cache.get(2))  # -1
    cache.put(4, 4)       # Evicts key 1
    print(cache.get(1))  # -1
    print(cache.get(3))  # 3
    print(cache.get(4))  # 4