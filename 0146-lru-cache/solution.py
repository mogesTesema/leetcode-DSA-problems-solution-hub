class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]

        # Move to front (most recently used)
        self._remove(node)
        self._add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            # Update existing node
            node = self.lookup[key]
            node.value = value

            # Move to front
            self._remove(node)
            self._add_to_front(node)
            return

        # Create new node
        node = Node(key, value)
        self.lookup[key] = node

        self._add_to_front(node)

        # Evict if needed
        if len(self.lookup) > self.capacity:
            # Remove least recently used (tail.prev)
            lru = self.tail.prev
            self._remove(lru)
            del self.lookup[lru.key]
