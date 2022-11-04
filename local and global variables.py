# lacal and global variable with different names
"""x = 123
def display():
    y = 244
    print(y)
print(x)
display()"""

# loacal and global variables with same name

"""x = 6554
def display():
    x = 345
    print(x)
    print(globals()['x'])
display()"""

# assigning a variable to a function
x = 234
def display():
    x = 567
    print(x)
    print(globals()['x'])
y = display
y()