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
newList = [x for x in thislist]
print("With List Comprehension: ", newList)
print("Printing newList at the line 36", newList)

newList.clear()
newList = [x for x in thislist if "a" in x]
print("With List Comprehension, only get items that contains 'a': ", newList)
print("Printing newList at the line 42", newList)

newList.clear()
newList = [x for x in range(10)]
print("Printing newList at the line 47", newList)
print("Printing one item per line")
[print(x) for x in newList]

"""
Expression

The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
"""
newList.clear()
newList = [x.upper() for x in thislist]
print("Printing newList at the line 56", newList)

"""
EThe expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
"""
newList.clear()
newList = [x if x != "banana" else "orange" for x in thislist]
print("Printing newList at the line 63", newList)
