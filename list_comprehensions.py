
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

ucfruits = [f.upper() for f in fruits]
print("ucfruits: {}\n".format(ucfruits))
#  [EXPR for VAR ... in ITERABLE]

long_fruits = [f.upper() for f in fruits if len(f) > 8]
print("long_fruits: {}\n".format(long_fruits))

long_fruits = [f for f in fruits if len(f) > 8]
print("long_fruits: {}\n".format(long_fruits))

lf_gen = (f for f in fruits if len(f) > 8)
print("lf_gen: {}".format(lf_gen))
print(next(lf_gen))
print()
for fruit in lf_gen:
    print(fruit)

g = (f.upper() for f in fruits)
e = enumerate(fruits)
print(next(e))
print(next(e))
print(g, e)
for i, fruit in e:
    print(i, fruit)
print(list(enumerate(fruits)))


print(next(g))
print(next(g))

print()
for thing in g:  # next(g), next(g), next(g), ...
    print(thing)

