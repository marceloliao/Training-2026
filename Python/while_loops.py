"""
Break statement

With the break statement we can stop the loop even if the while condition is true
"""

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

"""
Continue statement

With the continue statement we can stop the current iteration, and continue with the next
"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


"""
Else statement

With the else statement we can run a block of code once when the condition no longer is true
"""

i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break  # Note: The else block will NOT be executed if the loop is stopped by a break statement.
else:
    print("i is no longer less than 6")
