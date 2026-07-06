"""
A variable is created the moment you first assign a value to it.

Variables do not need to be declared with any particular type, and can even change type after they have been set.
"""

i = 4       # x is of type int
i = "Sally" # x is now of type str
print(i)
print(type(i))

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
