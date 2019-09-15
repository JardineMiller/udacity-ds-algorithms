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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_telemarketers(calls, texts):
    potentials = get_potential_telemarketers_from_calls(calls)
    filter_potentials_from_texts(texts, potentials)

    return potentials

def get_potential_telemarketers_from_calls(calls):
    potential_telemarketers = set()
    confirmed_not_telemarketers = set()

    for record in calls:
        from_num = record[0]
        to_num = record[1]

        confirmed_not_telemarketers.add(to_num)

        if (from_num not in confirmed_not_telemarketers):
            potential_telemarketers.add(from_num)

        potential_telemarketers.discard(to_num)

    return potential_telemarketers

def filter_potentials_from_texts(texts, potential_telemarketers):
    for record in texts:
        from_num = record[0]
        to_num = record[1]

        potential_telemarketers.discard(from_num)
        potential_telemarketers.discard(to_num)

def print_telemarketers(calls, texts):
    telemarketers = sorted(get_telemarketers(calls, texts))

    print("These numbers could be telemarketers: ")
    for t in telemarketers:
        print(t)

print_telemarketers(calls, texts)

# =============================#
# =========== TESTS ===========#
# =============================#
def test():
    calls_test = [
        ['123 456', '97424 22395', '01-09-2016 06:01:12', '186'],
        ['97424 22395', '123 456', '01-09-2016 06:03:51', '1975'], ['123 456', '456 789', '01-09-2016 06:03:51', '200'],
        ['(666)5678', '456 789', '01-09-2016 06:03:51', '200'],
        ['(666)1111', '456 789', '01-09-2016 06:03:51', '200'],
        ['(666)1111', '123 456', '01-09-2016 06:03:51', '200'],
        ['97424 22395', '(666)5678', '01-09-2016 06:03:51', '200'],
        ['1405678', '456 789', '01-09-2016 06:03:51', '200'],
        ['1405678', '(666)5678', '01-09-2016 06:03:51', '250'],
        ['1405678', '1405679', '01-09-2016 06:03:51', '250'],
        ['1405679', '(666)5678', '01-09-2016 06:03:51', '250'],
    ]

    texts_test = [
        ['97424 22395', '90365 06212', '01-09-2016 06:03:22'],
        ['94489 72078', '92415 91418', '01-09-2016 06:05:35'],
        ['81520 43406', '92421 64236', '01-09-2016 06:09:34'],
        ['97389 12538', '1405678', '01-09-2016 06:09:39'],
        ['81515 42171', '98440 02823', '01-09-2016 06:13:30'],
        ['78132 18081', '77956 90632', '01-09-2016 06:19:37'],
        ['90352 50054', '97389 12538', '01-09-2016 06:30:42'],
        ['90359 99240', '94491 55790', '01-09-2016 06:32:59'],
        ['78295 65598', '(666)1111', '01-09-2016 06:34:46'],
        ['93412 66159', '9845407778', '01-09-2016 06:36:15']
    ]

    result = set()

    assert(get_telemarketers(calls_test, texts_test) == result)

    print("all tests pass")

#test()