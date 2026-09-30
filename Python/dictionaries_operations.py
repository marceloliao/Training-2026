"""
Assessing items in dictionaries
"""

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)

"""
There is also a method called get() that will give you the same result
"""
y = thisdict.get("year")
print(y)

"""
Get Keys

The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
"""

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

"""
Get Values

The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
"""
car = {"brand": "Kia", "model": "Sorento", "year": 2020}

x = car.values()

print(x)  # before the change

car["year"] = 2024

print(x)  # after the change


"""
Get Items

The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
"""
y = car.items()
print(y)
print(type(y))

car["year"] = 2026
print(y)

"""
Check if Key Exists

To determine if a specified key is present in a dictionary use the 'in' keyword.
"""

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(
    "Yes, 'model' is one of the keys in the thisdict dictionary"
    if "model" in thisdict
    else "No, 'model' is NOT one of the keys in the thisdict dictionary"
)

"""
Update Dictionary

The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["brand"] = "Mercedez"
print(thisdict)

thisdict.update({"year": 2026})
print(thisdict)

"""
Add items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:
"""
thisdict["color"] = "blue"
print(thisdict)

"""
Or we can use update to add a new key, value pair
"""
thisdict.update({"engine": "hybrid"})
print(thisdict)


"""
Remove items

The pop() method removes the item with the specified key name.
"""
thisdict.pop("color")
print(thisdict)

"""
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
"""
thisdict.popitem()
print(thisdict)
thisdict.popitem()
print(thisdict)

"""
The del keyword removes the item with the specified key name.
"""
del thisdict["model"]
print(thisdict)

"""
The del keyword can also delete the dictionary completely.
"""

del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

"""
The clear() method empties the dictionary
"""

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)

"""
Loop through a dictionary

You can loop through a dictionary by using a 'for' loop.
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict:  # This only print out all keys
    print(f"This only print out keys: {x}")

# Same as the following
for x in thisdict.keys():
    print(x)

for x in thisdict:  # This only print out all values
    print(f"Printing the value: {thisdict[x]}")

# Same as the following
for x in thisdict.values():
    print(f"Printing the values: {x}")

# Print both keys and values
for x in thisdict.items():
    print(f"Printing the items: {x}")

"""
Copying a dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to 
dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(f"Making a copy using copy() method: {mydict}")

"""
Make a copy of a dictionary with the dict() function
"""
secondcopy = dict(thisdict)
print(f"Making a copy using dict() method: {secondcopy}")


"""
Nested dictionaries
"""
# Create a dictionary that contain three dictionaries
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

# Or, if you want to add three dictionaries into a new dictionary
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily = {"child1": child1, "child2": child2, "child3": child3}

# Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])

# Loop through a nested dictionary
for item in myfamily.items():
    print(f"Printing items in myfamily: {item}")

for key in myfamily.keys():
    print(f"Printing keys in myfamily: {key}")

for value in myfamily.values():
    print(f"Printing values in myfamily: {value}")

# Loop through the keys and values of all nested dictionaries
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])
