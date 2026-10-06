"""
Multiple Elif Statements

You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.
"""

# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

score = 75
print(score)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

"""
Logical operators

and, or, not
"""

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

if not a < b:
    print("a is not greater than b")

"""
Pass statement

The pass statement is useful in several situations:

    When you're creating code structure but haven't implemented the logic yet
    When a statement is required syntactically but no action is needed
    As a placeholder for future code during development
    In empty functions or classes that you plan to implement later
"""
age = 20

if age < 18:
    pass  # TODO: Add underage logic later
else:
    print("Access granted")
