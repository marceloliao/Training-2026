"""
DSA: Data Structures and Algorithms
"""

# Find the lowest value in an array

my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print("Lowest value:", minVal)
