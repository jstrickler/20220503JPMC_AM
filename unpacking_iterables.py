
x = [5, 10, 15]

a, b, c = x   # a = x[0], b = x[1], ...

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports.items(), '\n')

for abbr, name in airports.items():
    # abbr, name = next(airports.items())
    # ...
    print(abbr, name)
print()
