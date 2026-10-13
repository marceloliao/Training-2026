"""
Generators

Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

Generators Saves Memory

Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

For large datasets, generators save memory
"""


def count_up_to(n):
    numbers = []
    count = 1
    while count <= n:
        numbers.append(count)
        count += 1
    return numbers  # This consume a lot of memory if n is large, because it creates a list of all numbers up to n


for num in count_up_to(5):
    print(num)


def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # This will pause the function and return the current value of count, and when the function is called again, it will resume from where it left off
        count += 1


for num in count_up_to(5):
    print(num)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
    print(next(gen))
