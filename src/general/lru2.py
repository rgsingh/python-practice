
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node
        # Dummy head and tail to avoid edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used (right after head)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)


    @staticmethod
    def _remove(node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node



if __name__ == '__main__':
    cache = LRUCache2(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 1
    cache.put(3, 3)       # Evicts key 2
    print(cache.get(2))  # -1
    cache.put(4, 4)       # Evicts key 1
    print(cache.get(1))  # -1
    print(cache.get(3))  # 3
    print(cache.get(4))  # 4

