"""
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
"""

my_array = [7, 12, 9, 4, 11, 2]
lowest = my_array[0]

for i in my_array:
    if i < lowest:
        lowest = i
print("Lowest number is: ", lowest)
