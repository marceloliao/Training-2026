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
