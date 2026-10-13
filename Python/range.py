"""
range(start, stop, step)
"""

x = range(3, 10, 2)

# display x:
print(x)

# convert to list to display the content of x:
print(list(x))


# Using List to Display Ranges

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

# Slicing a Range
# Like other sequences, ranges can be sliced to extract a subsequence.

r = range(10)
print(r[2])
print(r[:3])
print(list(r[:3]))
