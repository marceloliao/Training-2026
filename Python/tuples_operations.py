thistuple = ("apple", "kiwi", "cherry", "banana", "watermelon")
print(thistuple)

"""
Tuple can be created without parentheses
"""
thistuple = "apple", "babana", "cherry"
print(thistuple)

"""
Tuple can contain duplactesbe
"""
thistuple = ("apple", "babana", "cherry", "apple")
print(thistuple)

"""
Tuple length can be found using len() function
"""
thistuple = ("apple", "babana", "cherry", "apple")
print(len(thistuple))

"""
Tuple can be of different data types
"""
thistuple = ("apple", 10, True, 3.14)
print(thistuple)

"""
Tuple can be created using tuple() constructor
"""
thistuple = tuple(("apple", 10, True, 3.14))
print(thistuple)

"""
Tuple can be indexed
"""
thistuple = ("apple", "babana", "cherry", "apple")
print(thistuple[0])
print(thistuple[-1])

"""
Create a tuple with one item
"""
thistuple = ("apple",)
print(thistuple)

"""
Create a tuple with no item
"""
thistuple = ()
print(thistuple)
print("Without any item, type of thistuple is", type(thistuple))

"""
Range of indexes in a tuple
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

"""
Range of negative indexes in a tuple
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

"""
Change tuple values
Once a tuple is created, you cannot change its values, not even to add or to remove, but there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "mango"
thistuple = tuple(y)
print(thistuple)

"""
Packing a tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
Example: thistuple = ("apple", "banana", "cherry")
"""

"""
Unpacking a tuple
In Python, we are also allowed to extract the values back into variables. This is called "unpacking".
"""
a, b, c = thistuple
print(a, b, c)

"""
Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
a, b, *c = thistuple
print(a, b, c)

d, *e, f = thistuple
print(d, e, f)

"""
Loop through a tuple
"""
for x in thistuple:
    print(x)

print(range(len(thistuple)))  # Return a range tuple
print(type(range(len(thistuple))))  # The type is range

for i in range(len(thistuple)):
    print(i, thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

"""
Join two tuples
"""
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
print(tuple3)

"""
Multiple tuples
"""
fruits = ("apple", "banana", "cherry")
two_fruits = fruits * 2
print(two_fruits)

"""
Tuple Methods

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""

print("The index of banana is", two_fruits.index("banana"))
