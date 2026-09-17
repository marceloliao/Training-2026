"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List: List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple: Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set: Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary: Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

"""

thislist = ["banana", "orange", "apple", "pineapple"]

print(thislist)
print(len(thislist))
print(type(thislist))
print("The first item is", thislist[0])
print("The first item from the right is", thislist[-1])

"""
Use the constructor list() to create a list.
"""
thislist2 = list(
    ("banana", "orange", "apple", "pineapple", "cherry")
)  # note the double round-brackets
print(thislist2)

"""
Use insert() method to insert an item at the specified index
"""
thislist2.insert(2, "watermelon")
print("After inserting 'watermelon': ", thislist2)

"""
Use append() method to add an item at the end of the list
"""
thislist2.append("kiwi")
print("After appending 'kiwi': ", thislist2)

"""
Use extend() method to append elements from another list to current list

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""
currentlist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
currentlist.extend(tropical)
print("After appending tropical list into current list: ", currentlist)

tropicaltuple = ("kiwi", "orange")
currentlist.extend(tropicaltuple)
print("After appending tropical tuple into current list: ", currentlist)

thisdict = {1: "strawberry", 2: "lichi"}

# currentlist.extend(thisdict)
# print("After appending thisdict into current list: ", currentlist)

"""
Use remove() method to remove an item from the list

If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
"""
currentlist.remove("kiwi")
print("After removing 'kiwi': ", currentlist)

"""
The pop() method removes the specified index, (or the last item if index is not specified)
"""
currentlist.pop()
print("After popping the last item: ", currentlist)

currentlist.pop(3)
print("After popping the thrid item: ", currentlist)

"""
The del() method also removes the specified index, but the method usage is different
"""
del currentlist[2]
print("After deleting the second item using del: ", currentlist)

"""
The clear() method empties the list
"""
currentlist.clear()
print("After clearing the list: ", currentlist)

"""
The del() method can also delete the list completely
"""
del currentlist
print("After deleting the list using del: ", currentlist)
