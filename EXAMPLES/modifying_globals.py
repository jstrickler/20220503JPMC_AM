
# x = 100

def spam():
    global x  # bad magic!! the dark side!!
    x = 42
    print("in spam: x is", x)

spam()
print("in main: x is", x)
