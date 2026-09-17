"""
Tuple: Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
"""

thistuple = ("apple", "kiwi", "cherry", "banana", "watermelon")
print(thistuple)

"""
Tuple can be created without parentheses
"""
thistuple = "apple", "babana", "cherry"
print(thistuple)

"""
Tuple can contain duplicates
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
thistuple = tuple(("apple", 10, True, 3.14))  # note the double round-brackets
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
