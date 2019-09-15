# Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

# Example 1:

# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:

# input = [9, 9, 9]
# output = [1, 0, 0, 0]
# Challenge:

# One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.

# But can you solve it in some other way?

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    return

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")  

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# This is fucking stupid