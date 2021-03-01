'''
import re

file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "regex_sum_42.txt"

try:
    fh = open(file_name)
except:
    print("Error: invalid file name")
    exit(-1)

txt = fh.read()
numbers = re.findall("[0-9]+", txt)
_sum = 0
for val in numbers:
    _sum += int(val)

print(_sum)
'''

import re 

print( sum( [ int(val) for val in re.findall( "[0-9]+", (open(input("Enter file name: "))).read()) ] ) )
