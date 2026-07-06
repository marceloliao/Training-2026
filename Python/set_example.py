print("Sets in Python")

my_set = {1, 2, 3, 3, "hello"}
print(my_set)  # {1, 2, 3, 'hello'} - duplicate 3 removed

my_set.add(4)
print(my_set)  # {1, 2, 3, 4, 'hello'} - duplicate 3 removed

my_set.remove(1)
print(my_set)  # {2, 3, 4, 'hello'} - duplicate 3 removed

# Set operations
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)  # Union: {1, 2, 3, 4}
print(set_a & set_b)  # Intersection: {2, 3}
print(set_a - set_b)  # Difference: {1}