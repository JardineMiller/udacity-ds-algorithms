# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head=None):
        if head is not None: 
            self.head = head
        else:
            self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.

    if list1 is None: 
        return list2
    if list2 is None:
        return list1

    result = LinkedList()

    list1_node = list1.head

    print("list1: ", list1)
    print("list1 head: ", list1.head)

    print("list2: ", list2)
    print("list2 head: ", list2.head)

    print("======")

    list2_node = list2.head

    while list1_node is not None or list2_node is not None:
        if list1_node is None:
            result.append(list2_node)
            list2_node = list2_node.next
        elif list2_node is None:
            result.append(list1_node)
            list1_node = list1_node.next
        elif list1_node.value <= list2_node.value:
            result.append(list1_node)
            list1_node = list1_node.next
        else:
            result.append(list2_node)
            list2_node = list2_node.next

    return result


linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

# merged = merge(linked_list, second_linked_list)
# print(str(merged))
    
# Lets make sure it works with a None list
# merged = merge(None, linked_list)
# print(str(merged))

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)

        return merge(node.value, self._flatten(node.next))


nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# First Test scenario
# linked_list = LinkedList(Node(1))
# linked_list.append(3)
# linked_list.append(5)

# nested_linked_list = NestedLinkedList(Node(linked_list))

# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)

# nested_linked_list.append(Node(second_linked_list))

solution = nested_linked_list.flatten()
# assert solution == [1,2,3,4,5]