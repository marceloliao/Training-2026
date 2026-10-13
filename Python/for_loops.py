fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

"""
Range function is used to generate a sequence of numbers
"""

for x in range(6):
    print(x, end=", ")

print()

for x in range(2, 6):
    print(x, end=", ")

print()
for x in "banana":
    print(x, end=", ")
