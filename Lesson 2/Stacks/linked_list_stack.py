class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.num_elements += 1
        return

    def pop(self):
        if self.is_empty():
            return None

        result = self.head.value
        self.head = self.head.next
        self.num_elements -= 1

        return result

    def is_empty(self):
        return self.num_elements is 0

    def size(self):
        return self.num_elements


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

def test(scenario, result, expected):
    scenario = "Scenario: " + scenario
    status = "Status: PASS" if result is expected else "Status: FAIL"
    result_str = "Result: " + str(result)
    expected_str = "Expected: " + str(expected)

    print(scenario)
    print(result_str)
    print(expected_str)
    print(status)
    print("============")

print("\n")
print("======= Running Tests =======")

# Test size
test("Size", stack.size(), 5)

# Test pop
test("Pop", stack.pop(), 50)

# # Test push
stack.push(60)
test("Push", stack.pop(), 60)
test("Push", stack.pop(), 40)
test("Push", stack.pop(), 30)

stack.push(50)
test("Size", stack.size(), 3)
print("======= Tests Complete =======")