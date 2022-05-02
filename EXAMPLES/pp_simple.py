#!/usr/bin/env python
"""
Parse a date in the form "MMM dd"  (using month abbreviations)
"""
import pyparsing as pp

# "bottom-up" grammar (not used by script)
"""
Date "bottom-up" grammar

Date ::= Month Day
Month ::= Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec
Day ::= nums
"""

def validate_date(tokens):
    """
    Make sure date token is in range 1-31.

    A 'real' version of this function would be called from Date,
    validate for each specific month length, and check for leap year.

    :param tokens: list of matched tokens for this element
    :return: None if valid
    """
    date = int(tokens[0])
    if (date < 0) or (date > 31):
        raise pp.ParseException("Date out of range")


Day = pp.Word(pp.nums)
Day.setParseAction(validate_date)
Month = pp.oneOf('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec')
Date = Month + Day

samples = [
    "Feb 2",
    "Mar 5",
    "Noz 18",
    "wombat",
    "Apr 3232",
]

for sample in samples:
    print(sample, end=' ')
    try:
        result = Date.parseString(sample)
    except pp.ParseException as err:
        print("oops!")
    else:
        print(result)
