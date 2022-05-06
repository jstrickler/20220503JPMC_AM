
def letters():
    for letter in 'c', 'd','e':
        yield letter

x = letters()
print(hasattr(x, '__iter__'))
print("x: {}".format(x))


for letter in x:
    print(letter)
