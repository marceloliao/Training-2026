"""
Set: Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Note: Set items are unchangeable, but you can remove items and add new items.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.
"""

"""
Duplicates Not Allowed
Duplicate values will be ignored

True and 1 is considered the same value and are treated as duplicates
False and 0 are considered the same value in sets, and are treated as duplicates:
"""
thisset = {"apple", "banana", "cherry", "cherry", 0, 1, True, False}
print(thisset)
print(len(thisset))  # Return the length of the set

"""
The set() constructor
"""
thisset = set(("pineapple", "orange", "lichi"))  # note the double round-brackets
print(type(thisset))
