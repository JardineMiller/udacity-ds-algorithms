# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    stack = Stack()
    
    #Iterate through equation checking parentheses
    for char in equation:
        if char is '(':
            stack.push(char)
        elif char is ')':
            if stack.pop() == None:
                return False

    #Return True if balanced and False if not
    return stack.size() is 0

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


test("Equation checker - Balanced", equation_checker('((3^2 + 8)*(5/2))/(2+6)'), True)
test("Equation checker - Unbalanced", equation_checker('((3^2 + 8)*(5/2))/(2+6))'), False)