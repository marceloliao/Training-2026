thislist = ["apple", "kiwi", "cherry", "banana", "watermelon"]
print(thislist)

"""
Sort List
"""
thislist.sort()
print(thislist)

numlist = [100, 50, 65, 82, 23]
numlist.sort()
print(numlist)

"""
Sort Descending
"""
thislist.sort(reverse=True)
print(thislist)

"""
Customize Sort Function
"""
print(numlist)


def myFunc(n):
    return abs(n - 50)


numlist.sort(key=myFunc)
print(numlist)

"""
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
"""

thislist.clear()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key=str.lower)
print(thislist)

"""
Reverse Order regardless of the alphabets
"""
thislist.reverse()
print(thislist)


"""
Copy List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2.
"""
thislist = ["apple", "banana", "cherry"]
newlist = thislist.copy()
print("After running the built-in copy method:", newlist)

"""
Using the list() constructor to make a copy:
"""
newlist2 = list(thislist)
print("After running the list() constructor:", newlist2)

"""
Using slice operator ':'
"""
newlist3 = thislist[:]
print("After running the slice operator:", newlist3)

"""
Join Lists
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("After running the '+' operator:", list3)

"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
"""

print("The index of cherry is :", thislist.index("cherry")) 