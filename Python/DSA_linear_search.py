"""
Linear Search

Linear search (or sequential search) is the simplest search algorithm. It checks each element one by one.
"""

"""
In Python, the fastest way check if a value exists in a list is to use the in operator.
"""

my_array = [3, 7, 2, 9, 5, 1, 8, 4, 6]
if 8 in my_array:
    print("8 Found")
else:
    print("8 not Found")

lowest = my_array[0]

for i in my_array:
    if i < lowest:
        lowest = i
print("Lowest number is: ", lowest)
"""
But if you need to find the index of a value, you will need to implement a linear search
"""


def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1


target = 53
result = linearSearch(my_array, target)

print(f"Target found at the index {result}" if result != -1 else "Target not found")
