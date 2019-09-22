# We have briefly discussed caching as part of a practice problem while studying hash maps.

# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. 
# If, however, the entry is not found, it is known as a cache miss.

# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full 
# and we want to add a new entry to the cache, we use some criteria to remove an element. 
# After removing an element, we use the put() operation to insert the new element. 
# The remove operation should also be fast.

# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. 
# An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
# For the current problem, consider both get and set operations as an use operation.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. 
# If the cache is full, you must write code that removes the least recently used entry first 
# and then insert the element.

# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.next = None
        self.previous = None
        self.value = value

class DLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elems = 0
    
    def add(self, new_node):
        new_node.previous = None
        new_node.next = None

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.num_elems += 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.num_elems += 1
        
    def remove_head(self):
        self.head.next.previous = None
        self.head = self.head.next
        self.num_elems -= 1

    def remove_node(self, node):        
        if self.get_head() == node and self.get_tail() == node:
            self.head = None
            self.tail = None
        elif self.get_head() == node:
            self.head = node.next
            node.next.previous = self.head
        elif self.get_tail() == node:
            self.tail = node.previous
            node.previous.next = self.tail
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        
        self.num_elems -= 1

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def size(self):
        return self.num_elems

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size = 0
        self.capacity = capacity
        self.store = {}
        self.access_list = DLinkedList()
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        entry = self.store.get(key, None)

        if entry:
            # Update the access list
            self.update_node_access(entry)
            return entry.value
        
        return -1

    def update_node_access(self, node):
        self.access_list.remove_node(node)
        self.access_list.add(node)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        new_node = Node(key, value)
        entry = self.store.get(key, None)

        if entry:
            # Update existing - no need to assess capacity
            self.update_node_access(entry)
            new_node.previous = self.access_list.get_tail().previous
            self.store[key] = new_node
            return

        # New entry - need to assess capacity
        if self.size == self.capacity:
            self.remove_last_used()

        # Add new entry
        self.access_list.add(new_node)
        self.store[key] = new_node
        self.size += 1

    def remove_last_used(self):
        # Removes the least recently used item from the cache
        removed = self.access_list.get_head()
        self.access_list.remove_head()
        self.store.pop(removed.key)
        self.size -= 1


#=============================# 
#=========== TESTS ===========#
#=============================#

separator = "--------------------------------------"

def test(scenario, result, expected):
    scenario = "Scenario: " + scenario
    status = "Status: PASS" if result is expected else "Status: FAIL"
    result_str = "Result: " + str(result)
    expected_str = "Expected: " + str(expected)

    print(scenario)
    print(result_str)
    print(expected_str)
    print(status)
    print(separator)

def run_linked_list_tests():
    print(separator)
    ll = DLinkedList()
    ll.add(Node(1, 1))
    ll.add(Node(2, 2))

    test("Linked List size()", ll.size(), 2)

    ll.remove_head()

    test("Linked List size() after head removed", ll.size(), 1)
    test("Linked List head after updated after head removed", ll.head.value, 2)

    ll.add(Node(3, 3))
    ll.add(Node(4, 4))
    ll.add(Node(5, 5))

    test("Linked List Size after adding more nodes", ll.size(), 4)
    test("Linked List tail", ll.tail.value, 5)

def run_LRU_cache_tests():
    print(separator)
    cache = LRU_Cache(5)

    test("LRU Cache size when empty", cache.size, 0)
    test("Cache get miss returns -1", cache.get(1), -1)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    test("LRU Cache size after 4 inserts returns 4", cache.size, 4)
    test("Cache get() from position 1 returns 1", cache.get(1), 1)
    test("Cache get() from position 2 returns 2", cache.get(2), 2)
    test("More cache misses return -1", cache.get(9), -1)

    cache.set(5, 5) 
    cache.set(6, 6)

    test("Size after reaching maximum capacity", cache.size, 5)
    test("Cache miss because we removed an entry due to reaching maximum capacity", cache.get(3), -1)
    test("Updated head", cache.access_list.get_head().value, 4)
    test("Updated tail", cache.access_list.get_tail().value, 6)

    cache.get(4)

    test("Updated head again", cache.access_list.get_head().value, 1)
    test("Updated tail again", cache.access_list.get_tail().value, 4)

def run_all_tests():
    print("=========== RUNNING TESTS ============")

    print("\n       SECTION: Linked Lists       ")
    run_linked_list_tests()

    print("\n       SECTION: LRU Cache       ")
    run_LRU_cache_tests()

    print("=========== TESTS COMPLETE ===========")


run_all_tests()
