thislist = ["apple", "kiwi", "cherry", "banana", "watermelon"]
for x in thislist:
    print(x)

print("--------------------------------")
for i in range(len(thislist)):
    print("Index", i, "is", thislist[i])

print("--------------------------------")
i = 0
while i < len(thislist):
    print("Index", i, "is", thislist[i])
    i += 1

print("--------------------------------")
"""
Looping Using List Comprehension

List Comprehension offers the shortest syntax for looping through lists
"""
print("List Comprehension")
[print(x) for x in thislist]

print("--------------------------------")
"""
Without List Comprehension
"""
newList = []
for x in thislist:
    newList.append(x)
print("Without List Comprehension: ", newList)

newList.clear()
print("With List Comprehension: ", [x for x in thislist])

newList.clear()
print(
    "With List Comprehension, only get items that contains 'a': ",
    [x for x in thislist if "a" in x],
)

newList.clear()
newList = [x for x in range(10)]
[print(x) for x in newList]
