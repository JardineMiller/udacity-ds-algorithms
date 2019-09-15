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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Run Time Analysis: 
# Simplified to O(1)

def print_first_text(record):
    print("First record of texts, {} texts {} at time {}".format(record[0], record[1], record[2]))

def print_last_call(record):
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(record[0], record[1], record[2], record[3]))

print_first_text(texts[0])
print_last_call(calls[-1])