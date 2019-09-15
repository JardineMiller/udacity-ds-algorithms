class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return
    
    def append(self, value):
        """ Append a value to the end of the list. """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = new_node
        self.length += 1
        return
        
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        
        node = self.head
        while node.next:
            if node.value is value:
                return node

            node = node.next

        return None
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        
        node = self.head
        prev = None

        # Assess first
        if node.value is value:
            self.head = node.next
            self.length -= 1
            return

        while node.next:
            if node.value is value:
                prev.next = node.next
                self.length -= 1
                return
                
            prev = node
            node = node.next

        # Assess last
        if node.value is value:
            prev.next = None
            self.length -= 1
    


    def pop(self):
        """ Return the first node's value and remove it from the list. """
    
        value = self.head.value
        self.remove(value)
        return value
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos > self.length - 1:
            self.append(value)
            return

        new_node = Node(value)

        if pos is 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return

        index = 0

        node = self.head
        prev = None

        while index < pos:
            prev = node
            node = node.next
            index += 1

        prev.next = new_node 
        new_node.next = node
        self.length += 1
        return
    
    def size(self):
        """ Return the size or length of the linked list. """
        return self.length
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
assert linked_list.search(10) == None, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"