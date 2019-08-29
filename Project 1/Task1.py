"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Run Time Analysis:
# Simplified to O(n) from O(n + m)

def add_to_distinct_from_list(list, distinct):
	for record in list:
		from_num = record[0]
		to_num = record[1]

		if (from_num not in distinct):
			distinct.add(from_num)

		if (to_num not in distinct):
			distinct.add(to_num)


def get_distinct_numbers(t_list, c_list):
	distinct_numbers = set()

	add_to_distinct_from_list(t_list, distinct_numbers)
	add_to_distinct_from_list(c_list, distinct_numbers)

	return distinct_numbers


def print_distinct_number_count(t_list, c_list):
	distinct_set = get_distinct_numbers(t_list, c_list)
	distinct_count = len(distinct_set)
	print("There are {} different telephone numbers in the records.".format(distinct_count)) 


print_distinct_number_count(texts, calls)

#=============================#
#=========== TESTS ===========#
#=============================#
def test_get_distinct_numbers():
	calls_test = [
		['123 456','98453 94494','01-09-2016 06:01:12','186'],
		['78298 91466','(022)28952819','01-09-2016 06:01:59','2093'],
		['97424 22395','(022)47410783','01-09-2016 06:03:51','1975'],
		['97424 22395','123 456','01-09-2016 06:03:51','1975']
	]

	texts_test = [
		['97424 22395','90365 06212','01-09-2016 06:03:22'],
		['94489 72078','92415 91418','01-09-2016 06:05:35'],
		['81520 43406','92421 64236','01-09-2016 06:09:34']
	]

	distinct = {
		'123 456',
		'98453 94494',
		'78298 91466',
		'(022)28952819',
		'97424 22395',
		'(022)47410783',
		'90365 06212',
		'94489 72078',
		'92415 91418',
		'81520 43406',
		'92421 64236'
	}

	assert(get_distinct_numbers(texts_test, calls_test) == distinct)

	print("all get_distinct_numbers tests pass")

 # test_get_distinct_numbers()
