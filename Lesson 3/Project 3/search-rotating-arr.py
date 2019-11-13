def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not len(input_list):
        return -1

    min = 0
    max = len(input_list) - 1

    pivot = get_pivot(input_list, min, max)

    if pivot < 0:
        return binary_search_recursive_soln(input_list, number, 0, len(input_list) - 1)

    if input_list[pivot] == number:
        return pivot
    
    if input_list[0] <= number:
        return binary_search_recursive_soln(input_list, number, 0, pivot - 1)

    return binary_search_recursive_soln(input_list, number, pivot + 1, len(input_list) - 1)

def binary_search_recursive_soln(array, target, low, high):
    mid = (low + high) // 2

    if array[mid] == target:
        return mid

    if low == high:
        return -1

    if target < array[mid]:
        high = mid - 1
        return binary_search_recursive_soln(array, target, low, high)

    if target > array[mid]:
        low = mid + 1
        return binary_search_recursive_soln(array, target, low, high)

def get_pivot(input_list, low, high):
    if low > high:
        return - 1

    if high == low:
        return high

    mid = (low + high) // 2

    if mid < high and input_list[mid] > input_list[mid + 1]:
        return mid
    if mid > low and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    if input_list[low] >= input_list[mid]: 
        return get_pivot(input_list, low, mid - 1)

    return get_pivot(input_list, mid + 1, high) 


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test(scenario, result, expected):
	separator = "-------------------------"
	scenario = "Scenario: " + scenario
	status = "Status: PASS" if result == expected else "Status: FAIL"
	result_str = "Result: " + str(result)
	expected_str = "Expected: " + str(expected)

	print(scenario)
	print(result_str)
	print(expected_str)
	print(status)
	print(separator)

test("Test 1", rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6), linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
test("Test 2", rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1), linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
test("Test 3", rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8), linear_search([6, 7, 8, 1, 2, 3, 4], 8))
test("Test 4", rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1), linear_search([6, 7, 8, 1, 2, 3, 4], 1))
test("Test 5", rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10), linear_search([6, 7, 8, 1, 2, 3, 4], 10))

test("Test unpivoted arr", rotated_array_search([1, 2, 3, 4, 5, 6, 7], 4), linear_search([1, 2, 3, 4, 5, 6, 7], 4))
test("Test empty arr", rotated_array_search([], 4), linear_search([], 4))
