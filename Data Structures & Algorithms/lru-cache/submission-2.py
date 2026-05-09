class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        # Pointers to previous and next nodes in the doubly linked list
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # Hash map allows O(1) access to any node in the linked list
        self.cache = {}  

        # Dummy nodes simplify edge cases (like inserting into an empty list)
        # We don't have to check if head/tail are None every time.
        # self.left = Least Recently Used (LRU) boundary
        # self.right = Most Recently Used (MRU) boundary
        self.left, self.right = Node(0, 0), Node(0, 0)
        
        # Initially connect the boundaries: left <-> right
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        """Helper function: Removes a node from anywhere in the doubly linked list."""
        prev, nxt = node.prev, node.next
        # Bypass the current node by linking its neighbors to each other
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        """Helper function: Inserts a node right before the right dummy node (MRU position)."""
        # Get the current last actual node (right before the dummy tail)
        prev, nxt = self.right.prev, self.right
        
        # Wire the new node to its neighbors
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        """Retrieves a value and marks it as recently used."""
        if key in self.cache:
            # If accessed, it becomes the Most Recently Used.
            # We must physically move it to the MRU position (the right).
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # Cache miss
        return -1

    def put(self, key: int, value: int) -> None:
        """Adds or updates a node, evicting the oldest node if capacity is breached."""
        if key in self.cache:
            # If the key already exists, remove the old node first.
            # The updated node will be re-inserted as MRU below.
            self.remove(self.cache[key])
            
        # Create the new node, store it in the map, and put it at the MRU position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Eviction policy: If we exceed capacity, drop the Least Recently Used item
        if len(self.cache) > self.cap:
            # The LRU node is always sitting right next to the left dummy node
            lru = self.left.next
            
            # Remove it from the linked list
            self.remove(lru)
            # Delete it from the hash map to free up the key
            del self.cache[lru.key]