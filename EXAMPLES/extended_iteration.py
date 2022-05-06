#!/usr/bin/env python
#
from itertools import chain, takewhile, dropwhile

spam = ['alpha', 'beta', 'gamma']
ham = 'delta', 'epsilon', 'zeta'
eggs = 'fried'

for letter in chain(spam, ham, eggs):  # <1>
    print(letter, end=' ')
print("\n")

eggs = [spam, ham]

for letter in chain.from_iterable(eggs):  # <2>
    print(letter, end=' ')
print("\n")

x = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
]
for thing in x:
    print(thing)
print()

for thing in chain.from_iterable(x):
    print(thing)
print()


fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

for fruit in takewhile(lambda f: len(f) > 4, fruits):  # <3>
    print(fruit, end=' ')
print("\n")

for fruit in takewhile(lambda f: f[0] != 'k', fruits):  # <4>
    print(fruit, end=' ')
print("\n")

values = [5, 18, 22, 31, 44, 57, 59, 61, 66, 70, 72, 78, 90, 99]

for value in dropwhile(lambda f: f < 50, values):  # <5>
    print(value, end=' ')
print("\n")
