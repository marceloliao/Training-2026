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
)  # If the item to remove does not exist, discard() will NOT raise an error.
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

# del thisset

print(thisset)

"""
Join sets

To add items from another set into the current set, use the update()or union () methods, both can add any iterable object (tuples, lists, dictionaries etc.)

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets, union() return a set, but update() doesn't

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# set1 = set1.update(set2)  # This syntax is wrong, using update() doesn't return anotehr set
# set1.update(set2)  # This syntax is correct
print("Using update(): ", set1)

set1 = set1.union(set2)
print("Using union(): ", set1)

set3 = set1 | set2
print("Using shorthand form of union(), which is a pipe '|' and create set3: ", set3)

"""
Intersection
"""
set1 = {"apple", "banana", "cherry", "google"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(f"Using intersection(): {set3}")

set4 = (
    set1 & set2
)  # The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
print(f"Using shorthand form of intersection(), which is '&' and create set4: {set4}")

"""
intersection_update()
The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
"""
set1.intersection_update(set2)
print(f"Using intersection_update(): {set1}")

"""
difference()
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
"""
set1 = {"apple", "banana", "cherry", "google"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(f"Using difference() and create set3: {set3}")

set4 = set1 - set2
print(f"Using shorthand form of difference(), which is '-' and create set4: {set4}")

"""
difference_update
Use the difference_update() method to keep only the items from the first set that are not present in the other set:
"""

set1.difference_update(set2)
print(f"Using difference_update() to update set1: {set1}")

"""
Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.
"""
set1 = {"apple", "banana", "cherry", "google"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(f"Using symmetric_difference() and creates set3: {set3}")

set4 = set1 ^ set2
print(
    f"Using shorthand form of symmetric difference(), which is '^' and create set4: {set4}"
)

"""
Set Methods

Method 	                Shortcut 	        Description
add()    	  	                                Adds an element to the set
clear() 	  	                                Removes all the elements from the set
copy() 	      	                                Returns a copy of the set
difference() 	                - 	            Returns a set containing the difference between two or more sets
difference_update() 	        -= 	            Removes the items in this set that are also included in another, specified set
discard() 	  	                                Remove the specified item
intersection() 	                & 	            Returns a set, that is the intersection of two other sets
intersection_update() 	        &= 	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint() 	  	                            Returns True if NO items of this set is present in another set
issubset()          	        <= 	            Returns True if all items of this set is present in another set
  	                            < 	            Returns True if all items of this set is present in another, larger set
issuperset() 	                >= 	            Returns True if all items of another set is present in this set
  	                            > 	            Returns True if all items of another, smaller set is present in this set
pop() 	  	                                    Removes an element from the set
remove() 	  	                                Removes the specified element
symmetric_difference() 	        ^ 	            Returns a set with the symmetric differences of two sets
symmetric_difference_update() 	^= 	            Inserts the symmetric differences from this set and another
union() 	                    | 	            Return a set containing the union of sets
update() 	                    |= 	            Update the set with the union of this set and others

"""
