class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    def to_list(self):
        list = []

        for node in self:
            list.append(node.value)

        return list

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    union_list = LinkedList()

    for node in llist_1:
        union_list.append(node.value)

    for node in llist_2:
        union_list.append(node.value)

    return union_list

def intersection(llist_1, llist_2):
    intersection_list = LinkedList()
    llist_1_list = llist_1.to_list()

    for node in llist_2:
        if node.value in llist_1_list:
            intersection_list.append(node.value)
            llist_1_list.remove(node.value)

    return intersection_list

def test(scenario, result, expected, reason = None):
    separator = "-------------------------"
    scenario = "Scenario: " + scenario
    status = "Status: PASS" if result == expected else "Status: FAIL"
    result_str = "Result: " + str(result)
    expected_str = "Expected: " + str(expected)

    print(scenario)
    print(result_str)
    print(expected_str)
    print(status)
    if reason:
        print("Reason: because " + reason)
    print(separator)
    
        
# Edge Test 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,3,3,3,1]
element_2 = [3,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

test_1_list_union = element_1 + element_2
test_1_ll_union = union(linked_list_1,linked_list_2).to_list()

test_1_list_intersection = list(filter(lambda x: x in element_1, element_2)) # This doesn't actually provide a true intersection, but my LL implementation does.
test_1_ll_intersection = intersection(linked_list_1,linked_list_2).to_list()

test("Union with many duplicates", test_1_ll_union, test_1_list_union)
test("Intersection Edge Test", test_1_ll_intersection, test_1_list_intersection, "there is only a single complete set of 3's in the two lists")

# Edge Test 2 - Proving that ordering of iterators does not matter
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,1]
element_2 = [3,3,3,3,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

test_1_list_union = element_1 + element_2
test_1_ll_union = union(linked_list_1,linked_list_2).to_list()

test_1_list_intersection = list(filter(lambda x: x in element_2, element_1)) # This doesn't actually provide a true intersection, but my LL implementation does.
test_1_ll_intersection = intersection(linked_list_1,linked_list_2).to_list()

test("Union with many duplicates", test_1_ll_union, test_1_list_union)
test("Intersection Edge Test", test_1_ll_intersection, test_1_list_intersection, "there is only a single complete set of 3's in the two lists and the order in which we iterate the lists does not matter")

# Edge Test 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

test_1_list_union = element_1 + element_2
test_1_ll_union = union(linked_list_1,linked_list_2).to_list()

test_1_list_intersection = list(filter(lambda x: x in element_1, element_2))
test_1_ll_intersection = intersection(linked_list_1,linked_list_2).to_list()

test("Empty Union", test_1_ll_union, test_1_list_union)
test("Empty Intersection", test_1_ll_intersection, test_1_list_intersection)

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

test_1_list_union = element_1 + element_2
test_1_ll_union = union(linked_list_1,linked_list_2).to_list()

test_1_list_intersection = list(filter(lambda x: x in element_1, element_2))
test_1_ll_intersection = intersection(linked_list_1,linked_list_2).to_list()

test("Union", test_1_ll_union, test_1_list_union)
test("Intersection", test_1_ll_intersection, test_1_list_intersection)

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test_1_list_union = element_1 + element_2
test_1_ll_union = union(linked_list_3,linked_list_4).to_list()

test_1_list_intersection = list(filter(lambda x: x in element_1, element_2))
test_1_ll_intersection = intersection(linked_list_3,linked_list_4).to_list()

test("Union", test_1_ll_union, test_1_list_union)
test("Intersection", test_1_ll_intersection, test_1_list_intersection)