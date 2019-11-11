def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = 0
    max = 0

    if not len(ints):
        return None

    for num in ints:
        if type(num) is not int and type(num) is not float:
            raise ValueError("Input must be a number")

        if num < min:
            min = num
        
        if num > max:
            max = num

    return (min, max)

## Example Test Case of Ten Integers
import random



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
    ints = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(ints)

    # Happy path
    test("array of 0-9 returns (0,9)", get_min_max(ints), (0,9))

    ints = [i for i in range(-10, 10)]  # a list containing 0 - 9
    random.shuffle(ints)

    # Handles negatives
    test("array of 0-9 returns (-10,9)", get_min_max(ints), (-10,9))

    ints = ["a" for i in range(0, 10)]  # a list containing 0 - 9

    try:
        get_min_max(ints)
    except ValueError:
        test("function handles incorrect type", True, True)

    ints = []
    test("empty arr returns None", get_min_max(ints), None)

run_tests()