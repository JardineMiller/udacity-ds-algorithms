"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import datetime
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Run Time Analysis:
# Simplified to O(n) from O(2n)

def to_dictionary(list):
    total_mins_by_number = {}

    for record in list:
        from_num = record[0]
        to_num = record[1]
        duration = record[-1]

        if (from_num not in total_mins_by_number):
            total_mins_by_number[from_num] = 0

        if (to_num not in total_mins_by_number):
            total_mins_by_number[to_num] = 0

        total_mins_by_number[from_num] += int(duration)
        total_mins_by_number[to_num] += int(duration)

    return total_mins_by_number

def get_total_minutes_by_number(c_list):
    total_mins_by_number = to_dictionary(c_list)
    return total_mins_by_number

def get_most_active_caller(c_list):
    total_mins_by_number = get_total_minutes_by_number(c_list)
    most_active_number = max(total_mins_by_number, key = total_mins_by_number.get)

    return (most_active_number, total_mins_by_number[most_active_number])

most_active_caller = get_most_active_caller(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(most_active_caller[0], most_active_caller[1]))

#=============================#
#=========== TESTS ===========#
#=============================#
def test():
    calls_test = [
        ['123 456', '97424 22395', '01-09-2016 06:01:12', '186'],
        ['97424 22395', '123 456', '01-09-2016 06:03:51', '1975'],
        ['123 456', '456 789', '01-09-2016 06:03:51', '200']
    ]

    result = {
        '97424 22395': 2161,
        '123 456': 2361,
        '456 789': 200
    }

    assert(get_total_minutes_by_number(calls_test) == result)
    assert(get_most_active_caller(calls_test) == ('123 456', 2361))

    print("all tests pass")

# test()

