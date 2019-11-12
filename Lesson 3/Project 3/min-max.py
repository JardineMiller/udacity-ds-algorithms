def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None

    if not len(ints):
        return None

    for num in ints:
        if type(num) is not int and type(num) is not float:
            raise ValueError("Input must be a number")

        if min is None or num < min:
            min = num

        if max is None or num > max:
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
    
    # Happy path
    ints = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(ints)
    test("array of 0-9 returns (0,9)", get_min_max(ints), (0,9))

    # Range starts > 0
    ints = [i for i in range(1, 6)]  # a list containing 1 - 5
    random.shuffle(ints)
    test("array of 1-5 returns (1,5)", get_min_max(ints), (1,5))

    # Range entirely negative
    ints = [i for i in range(-5, 0)]  # a list containing -1 - -5
    random.shuffle(ints)
    test("array of minus 1 to minus 5 returns (-5,-1)", get_min_max(ints), (-5,-1))

    # Handles negatives
    ints = [i for i in range(-10, 10)]  # a list containing -10 to 10
    random.shuffle(ints)
    test("array of 0-9 returns (-10,9)", get_min_max(ints), (-10,9))

    # Handles errors
    ints = ["a" for i in range(0, 10)]  # a list containing 0 - 9

    try:
        get_min_max(ints)
    except ValueError:
        test("function handles incorrect type", True, True)

    ints = []
    test("empty arr returns None", get_min_max(ints), None)

run_tests()