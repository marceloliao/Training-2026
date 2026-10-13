"""
DSA: Data Structures and Algorithms
"""

# Find the lowest value in an array
my_array = [7, 2, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print("Lowest value:", minVal)

"""
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""

# Implementation using a For loop
prev1 = 0
prev2 = 1
print("Fibonacci sequence using a For loop: ", end="")
print(prev1, end=", ")
print(prev2, end=", ")

for i in range(18):
    fibo = prev1 + prev2
    print(fibo, end=", ")
    prev1 = prev2
    prev2 = fibo

# Implementation using a recursion
# Recursion is when a function calls itself.
print()
print("Fibonacci sequence using a recursion: ", end="")
print(0, end=", ")
print(1, end=", ")

count = 2


def fibonacci(prev1, prev2):
    global count
    if count < 20:
        fibo = prev1 + prev2
        print(f"counter: {count} - fibo: {fibo}", end=", ")
        count += 1
        fibonacci(prev2, fibo)


fibonacci(0, 1)


# Finding The nth Fibonacci Number Using Recursion
def fibonacci_nth(n):
    if n <= 1:
        # print(n, end=", ")
        return n
    else:
        # print(fibonacci_nth(n - 1) + fibonacci_nth(n - 2), end=", ")
        return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)


print(fibonacci_nth(19))
