"""
Dictionary Items

Dictionary items are ordered, changeable, and do not allow duplicates.
"""

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

print(thisdict["model"])

"""
Dictionaries cannot have two items with the same key, duplicate values will overwrite existing values.
In the example below, only the 2026 will be preserved
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2026}
print(thisdict)

"""
Dictionary Items - Data Type
The values in dictionary items can be of any data type
"""
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(thisdict["colors"])
print(thisdict["colors"][2])

"""
The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.
"""
employee = dict(name="John", age=36, country="France")
print(employee)
