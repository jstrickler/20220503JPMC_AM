import csv
from collections import namedtuple

x = ['a', 'b', 'c']
for letter in x:
    print(letter)
print()

r = range(3)
for n in r:
    print(n)
print()

e = enumerate(x)
print(next(e))
print(next(e))
print(next(e))
# print(next(e))
print()

e = enumerate(x)
while True:
    try:
        print(next(e))
    except StopIteration:
        break
print()

x_iter = iter(x)
print(next(x_iter))
print(next(x_iter))
# iter() returns the iterator from an iterable


with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    headers = next(rdr)
    President = namedtuple('President', headers)
    print("headers: {}".format(headers))

    presidents = []
    for row in rdr:
        president = President(*row)
        presidents.append(president)

for president in presidents:
    print(president.first_name, president.last_name)