"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from enum import Enum
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
   
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_percentage_of_calls_for_codes(from_code, to_code, records):
    from_code_type = get_code_type(from_code)
    to_code_type = get_code_type(to_code)

    calls_from_code = filter_by(records, from_code, from_code_type)
    calls_to_code = filter_by(calls_from_code, to_code, to_code_type, False)

    total = len(calls_from_code)
    subset = len(calls_to_code)

    result = round(subset / total * 100, 2)
    return result

def print_area_calls_percentage(from_area, from_code, to_area, to_code, records):
    percentage = get_percentage_of_calls_for_codes(from_code, to_code, records)

    print("{}% percent of calls from fixed lines in {} are calls to other fixed lines in {}.".format(percentage, from_area, to_area))

def get_code_type(code):
    if ('(' in code and ')' in code):
        return NumberType.FIXED
    elif (' ' in code):
        return NumberType.MOBILE
    else:
        return NumberType.TELEMARKETER

def print_unique_codes_called_for(area_name, code, records, use_from_num=True):
    code_type = get_code_type(code)
    filtered_nums = filter_by(records, code, code_type, use_from_num)

    unique = sorted(get_unique_codes(filtered_nums, not use_from_num))

    print("The numbers called by people in {} have codes:".format(area_name))
    for u in unique:
        print(u)


class NumberType(Enum):
    FIXED = 1,
    MOBILE = 2,
    TELEMARKETER = 3


def filter_by_fixed(records, code, filter_index):
    filtered_list = []

    for record in records:
        if (code in record[filter_index]):
            filtered_list.append(record)

    return filtered_list


def filter_by_mobile(records, code, filter_index):
    filtered_list = []

    for record in records:
        num = record[filter_index]
        space_index = num.find(" ")

        if (space_index < 0):
            continue

        substr = num[:space_index]

        if (code == substr):
            filtered_list.append(record)

    return filtered_list


def filter_by_telemarketer(records, code, filter_index):
    filtered_list = []
    prefix_length = 3

    for record in records:
        num = record[filter_index]
        num_prefix = num[:prefix_length]

        if (num_prefix == code):
            filtered_list.append(record)

    return filtered_list


def filter_by(records, code, num_type, use_from_num=True):
    filter_index = 0 if use_from_num else 1

    if (num_type is NumberType.FIXED):
        filtered_list = filter_by_fixed(records, code, filter_index)
    elif (num_type is NumberType.MOBILE):
        filtered_list = filter_by_mobile(records, code, filter_index)
    elif (num_type is NumberType.TELEMARKETER):
        filtered_list = filter_by_telemarketer(records, code, filter_index)
    else:
        raise Exception('num_type not recognised: {}'.format(num_type))

    return filtered_list


def get_code(tel_number):
    if ('(' in tel_number):
        return tel_number[tel_number.find('('):tel_number.find(')') + 1]
    elif (' ' in tel_number):
        return tel_number[:4]
    else:
        return tel_number[:3]

def get_unique_codes(records, use_from_num=True):
    unique_codes = set()
    filter_index = 0 if use_from_num else 1

    for record in records:
        code = get_code(record[filter_index])
        unique_codes.add(code)

    return unique_codes

print_unique_codes_called_for("Bangalore", "(080)", calls, True)
print_area_calls_percentage("Bangalore", "(080)", "Bangalore", "(080)", calls)

# =============================#
# =========== TESTS ===========#
# =============================#
def test():
    calls_test = [
        ['123 456', '97424 22395', '01-09-2016 06:01:12', '186'],
        ['97424 22395', '123 456', '01-09-2016 06:03:51', '1975'],
        ['123 456', '456 789', '01-09-2016 06:03:51', '200'],
        ['(666)5678', '456 789', '01-09-2016 06:03:51', '200'],
        ['123 456', '(666)5678', '01-09-2016 06:03:51', '200'],
        ['1405678', '456 789', '01-09-2016 06:03:51', '200'],
        ['1405678', '(666)5678', '01-09-2016 06:03:51', '250'],
    ]

    filter_by_to_mobile_result = [
        ['123 456', '456 789', '01-09-2016 06:03:51', '200'],
        ['(666)5678', '456 789', '01-09-2016 06:03:51', '200'],
        ['1405678', '456 789', '01-09-2016 06:03:51', '200'],
    ]

    filter_by_tele_result = [
        ['1405678', '456 789', '01-09-2016 06:03:51', '200'],
        ['1405678', '(666)5678', '01-09-2016 06:03:51', '250'],
    ]

    filter_by_fixed_result = [
        ['(666)5678', '456 789', '01-09-2016 06:03:51', '200'],
    ]

    filter_by_mobile_result = [
        ['97424 22395', '123 456', '01-09-2016 06:03:51', '1975'],
    ]

    unique_from = [
        '123',
        '(666)',
        '140',
    ]

    unique_to = [
        '456'
    ]

    assert (filter_by(calls_test, '666', NumberType.FIXED) == filter_by_fixed_result)
    assert (filter_by(calls_test, '97424', NumberType.MOBILE) == filter_by_mobile_result)
    assert (filter_by(calls_test, '456', NumberType.MOBILE, False) == filter_by_to_mobile_result)
    assert (filter_by(calls_test, '140', NumberType.TELEMARKETER) == filter_by_tele_result)

    assert (get_unique_codes(filter_by_to_mobile_result) == unique_from)
    assert (get_unique_codes(filter_by_to_mobile_result, False) == unique_to)

    assert (get_percentage_of_calls_for_codes('123', '456', calls_test) == 33.33)

    print("all tests pass")

#test()
