"""
Linear Search

Linear search (or sequential search) is the simplest search algorithm. It checks each element one by one.
"""

"""
In Python, the fastest way check if a value exists in a list is to use the in operator.
"""

my_array = [7, 12, 9, 4, 11, 2]
if 4 in my_array:
    print("4 Found")
else:
    print("4 not Found")

lowest = my_array[0]

for i in my_array:
    if i < lowest:
        lowest = i
print("Lowest number is: ", lowest)
