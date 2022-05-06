g = globals()

g['animal'] = 'wombat'

print(animal)

g['bark'] = lambda : print("WOOF WOOF")

bark()

data = 1, 2, 3
print(list(map(lambda x: x * 10, data)))

scream = lambda : print("AIIEEEEEEEEE")
scream()












print('-' * 60)
global_things = dict(g)
for name, value in global_things.items():
    print(f"{name:20.20s} {str(value):30.30s}")