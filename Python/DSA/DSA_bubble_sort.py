# Sort the array using bubble sort
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
my_sortedarray = my_array.sort()
print(my_array)
print(my_sortedarray)

length = len(my_array)
print(f"length: {length}")
myindex = range(length - 1)
print(f"myindex: {myindex}")

for i in range(length - 1):
    for j in range(length - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            # the notation above swaps the values of the two variables at the same time
            # temp = my_array[j]
            # my_array[j] = my_array[j + 1]
            # my_array[j + 1] = temp


print(my_array)

"""
Bubble Sort Improvement

Imagine that the array is almost sorted already, with the lowest numbers at the start, like this for example:
my_array = [7, 3, 9, 12, 11]

In this case, the array will be sorted after the first run, but the Bubble Sort algorithm will continue to run, without swapping elements, and that is not necessary.

If the algorithm goes through the array one time without swapping any values, the array must be finished sorted, and we can stop the algorithm, like this:
"""

my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)
