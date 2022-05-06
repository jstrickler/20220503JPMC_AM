class Animal:
    pass

class Cat:
    def meow(self):
        print("meow meow")

c = Cat()
c.meow()

class_name = "Dog"
bark_method = lambda self: print("woof! woof!")

Dog = type(class_name, (Animal,),
           {'bark': bark_method})

d = Dog()
d.bark()

print(type(Cat), type(Dog), type(type))
print(type(c), type(d))

