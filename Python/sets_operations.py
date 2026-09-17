thisset = set(("pineapple", "orange", "lichi"))  # note the double round-brackets
print(thisset)
print(type(thisset))

"""
Loop through the set and print its values
"""
for x in thisset:
    print(x)

"""
Check if an item is present in a set, or not present in a set
"""
print("banana" in thisset)
print("banana" not in thisset)

"""
Once a set is created, you cannot change its items, but you can add new items.
"""
thisset.add("banana")
print(thisset)

"""
Add sets

To add items from another set into the current set, use the update() method, update() can add any iterable object (tuples, lists, dictionaries etc.)
"""
thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
tropical = ["pineapple", "mango", "papaya"]
thisset.update(tropical)
print(thisset)

"""
Remove item
To remove an item in a set, use the remove(), or the discard() method.
"""
thisset.remove("banana")
print(thisset)
# thisset.remove("banana")  # If the item to remove does not exist, remove() will raise an error.
print(thisset)
thisset.discard(
    "papaya"
)  # If the item to remove does not exist, remove() will NOT raise an error.
print(thisset)

"""
Can use pop() to remove a random item, because Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
"""
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

"""
Same as for lists, clear() clears all items
"""
thisset.clear()

print(thisset)

"""
Same as for lists, the del keyword will delete the set completely
"""
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
