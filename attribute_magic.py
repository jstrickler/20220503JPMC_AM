from types import MethodType
from president import President

p = President(26)

print(p.first_name, p.last_name, '\n')

fields = ['first_name', 'last_name', 'party']

for field in fields:
    print(getattr(p, field))
print()

x = p.birth_place
x = getattr(p, 'birth_place')
print(x)

# getattr() hasattr() setattr() delattr()

a = 52
b = "abc"
print(hasattr(a, '__iter__'))
print(hasattr(b, '__iter__'))

print(hasattr(a, 'to_json'))

def wombat(self):
    print("Darn this Congress!!")

setattr(President, 'complain', wombat)

p.complain()

def box(self):
    print("punch punch punch")

setattr(p, 'box', MethodType(box, p))

p.box()

print('-' * 60)
print(dir(p))




