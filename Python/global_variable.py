"""
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc() 

"""
If you create a variable with the same name inside a function, this variable will be local, and 
can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value.
"""

# y = "awesome"

# def myfunc2():
#   y = "fantastic"
#   print("Python is " + y)

# myfunc2()

# print("Python is " + y) 

"""
Also, use the global keyword if you want to change a global variable inside a function.
"""

z = "awesome"
print("Python is " + z) 

def myfunc3():
  global z
  z = "fantastic"

myfunc3()

print("Python is " + z) 