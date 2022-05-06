#!/usr/bin/env python
from pyparsing import *

'''  # <1>
grammar:
ssn = nums+ dash nums+ dash nums+
dash = '-'
nums = '0' | '1' | '2' etc etc
'''

dash = '-'  # <2>
number_a = Word(nums, exact=3)('number_a')
number_b = Word(nums, exact=2)('number_b')
number_c = Word(nums, exact=4)('number_c')

ssn_parser =     (
    number_a
    + Suppress(dash)
    + number_b
    + Suppress(dash)
    + number_c
)

input_string = """
    xxx 215-72-8314 yyy
    102-46-6919 zzz 182-19-2201
"""

for match in ssn_parser.searchString(input_string):  # <5>
    print(match)
    print(match.number_a, match.number_b)


