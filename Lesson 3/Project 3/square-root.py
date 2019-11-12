def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or (type(number) != int and type(number) != float):
        raise ValueError("number was null or the incorrect type")

    if number is 0 or number is 1:
        return number
    
    min = 1
    max = number

    while min <= max:
        mid = (min + max) // 2

        if mid * mid == number:
            return mid

        if mid * mid  < number:
            min =  mid + 1
            result = mid
        else:
            max = mid - 1
    
    return result

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

test("square root of 9 is 3", sqrt(9), 3)
test("square root of 0 is 0", sqrt(0), 0)
test("square root of 16 is 4", sqrt(16), 4)
test("square root of 1 is 1", sqrt(1), 1)
test("square root of 27 is floored to 5", sqrt(27), 5)
test("square root of 1,000,000 is 1,000", sqrt(1000000), 1000)

try:
    sqrt("a")
except ValueError:
    test("invalid input throws exception", True, True)