#!/usr/bin/env python

values = ['a', 'b', 'c', 'd', 'e', 'f']  # <1>

x, y, *z = values  # <2>
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

x, *y, z = values  # <2>
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

*x, y, z = values  # <2>
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]



for first_name, last_name, *_ in people:  # <3>
    print(first_name, last_name)
print()
