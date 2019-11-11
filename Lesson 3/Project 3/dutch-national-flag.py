def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    min_pos = 0
    max_pos = len(input_list) - 1
    
    i = 0
    
    while i <= max_pos:
        if input_list[i] is None or type(input_list[i]) is not int:
            raise ValueError("input list must contain only ints between 0 and 2")

        if input_list[i] < 0 or input_list[i] > 2:
            raise ValueError("following rules have not been met: 0 <= entry <= 2")

        if input_list[i] is 0:
            input_list[i] = input_list[min_pos]
            input_list[min_pos] = 0
            min_pos += 1
            i += 1
            continue
        
        if input_list[i] is 2:
            input_list[i] = input_list[max_pos]
            input_list[max_pos] = 2
            max_pos -= 1
            continue
            
        i += 1

    return input_list

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

test("array 1", sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]), sorted([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
test("array 2", sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]), sorted([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
test("array 3", sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]), sorted([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
test("empty array returns empty array", sort_012([]), [])

try:
    sort_012([0,1,2,3])
except ValueError:
    test("throws exception when invalid num present in array", True, True)