from operator import add


a = 10
b = 15

print("a + b: {}".format(a + b))
print("add(a, b): {}".format(add(a, b)))

def doit(x, y, func):
    return func(x, y)

def add_them(a, b):
    return a + b

print(doit(10, 20, add_them))
print(doit(10, 20, lambda a, b: a + b))
print(doit(10, 20, add))  # operator.add