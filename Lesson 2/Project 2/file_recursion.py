import os

def find_files(suffix, path):
	"""
	Find all files beneath path with file name suffix.

	Note that a path may contain further subdirectories
	and those subdirectories may also contain further subdirectories.

	There are no limit to the depth of the subdirectories can be.

	Args:
	  suffix(str): suffix if the file name to be found
	  path(str): path of the file system

	Returns:
	   a list of paths
	"""

	paths = []

	items = os.listdir(path)

	for item in items:
		extended_path = path + "/" + item

		if os.path.isfile(extended_path) and extended_path.endswith(suffix):
				paths.append(extended_path)
		elif os.path.isdir(extended_path):
			paths += find_files(suffix, extended_path)

	return paths

def test(scenario, result, expected):
	separator = "-------------------------"
	scenario = "Scenario: " + scenario
	status = "Status: PASS" if result is expected else "Status: FAIL"
	result_str = "Result: " + str(result)
	expected_str = "Expected: " + str(expected)

	print(scenario)
	print(result_str)
	print(expected_str)
	print(status)
	print(separator)

def run_tests():
	test("find_files with .c suffix returns 4 results", len(find_files(".c", "./testdir")), 4)
	test("find_files with .h suffix returns 4 results", len(find_files(".h", "./testdir")), 4)
	test("find_files with .gitkeep suffix returns 4 results", len(find_files(".gitkeep", "./testdir")), 2)

run_tests()