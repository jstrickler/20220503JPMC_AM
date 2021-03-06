#!/usr/bin/env python

def void(thing_being_decorated):
    return 42  # <1>

name = "Guido"
name = void(name)

@void  # <2>
def hello():
    print("Hello, world")
# hello = void(hello)

@void
def howdy():
    print("Howdy, world")

print(hello, type(hello)) # <3>
print(howdy, type(howdy)) # <3>
print(name, type(name))
