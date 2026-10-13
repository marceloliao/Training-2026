"""
Lambda Functions

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments: expression
"""

x = lambda a: a + 10
print(x(5))  # Output: 15

y = lambda a, b: a * b
print(y(5, 6))  # Output: 30


"""
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number: 
"""


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(
    3
)  # Or, use the same function definition to make both functions, in the same program

print(mydoubler(11))
print(mytripler(11))  # Output: 33

""" 
Lambda with Built-in Functions

Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
"""

# map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
doubled2 = [x * 2 for x in numbers]  # List comprehension alternative
print(doubled)
print(doubled2)

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
evens2 = [x for x in numbers if x % 2 == 0]
print(evens)
print(evens2)

# sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])

# sorted_by_age = sorted([y[1] for y in students])
# print(f"Sorted by age:{sorted_by_age}")
sorted_students2 = [student for student in sorted(students, key=lambda x: x[1])]
sorted_students3 = students.sort(key=lambda x: x[1])
print(sorted_students)
print(sorted_students2)
print(sorted_students3)
