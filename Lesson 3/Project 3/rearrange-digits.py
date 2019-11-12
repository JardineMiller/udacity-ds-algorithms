def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        raise ValueError("input list must not be null")

    if len(input_list) <= 1:
        return input_list

    sorted_list = mergesort(input_list)
    return rearrange(sorted_list)


def rearrange(sorted_list):
    # Should return an array of two entries
    result = []

    runner_one = len(sorted_list) - 1
    runner_two = len(sorted_list) - 2

    num_one = ""
    num_two = ""

    while runner_one >= 0 or runner_two >= 0:
        if (runner_one >= 0):
            num_one += str(sorted_list[runner_one])
            runner_one -= 2

        if (runner_two >= 0):
            num_two += str(sorted_list[runner_two])
            runner_two -= 2 

    num_one = int(num_one)
    num_two = int(num_two)

    result.append(num_one)
    result.append(num_two)

    return result


def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    merged = []

    left_index = 0
    right_index = 0

    while (left_index < len(left) and right_index < len(right)):

        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged
        

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

def run_tests():
    # Merge sort tests
    test("mergesort actually works 1", mergesort([4, 6, 2, 5, 9, 8]), sorted([4, 6, 2, 5, 9, 8]))
    test("mergesort actually works 2", mergesort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Rearrange
    test("test rearrange odd number of elems", rearrange_digits([1, 2, 3, 4, 5]), [531, 42])
    test("test rearrange even number of elems", rearrange_digits([4, 6, 2, 5, 9, 8]), [964, 852])
    test("test rearrange only 2 elements", rearrange_digits([9, 1]), [9, 1])

    # Edge case
    test("test rearrange only 1 element", rearrange_digits([9]), [9])
    test("test rearrange empty input", rearrange_digits([]), [])
    try:
        rearrange_digits(rearrange_digits(None))
    except ValueError:
        test("None input throws exception", True, True)


run_tests()