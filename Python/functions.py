"""
Keyword Arguments
You can send arguments with the key = value syntax.
"""


def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)


my_function(animal="dog", name="Buddy")

"""
Positional Arguments

When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:
"""


def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)


my_function("cat", "Toby")


# Sending a dictionary as an argument
def print_person(person):
    print("Name:", person["name"])
    print("Age:", person["age"])


my_person = {"name": "John", "age": 30}
print_person(my_person)

"""
Positional-Only Arguments

To specify positional-only arguments, add , / after the arguments
"""


def my_function(name, /):
    print("Hello", name)


my_function("Alice")  # Valid
# my_function(name="Alice")  # This will raise a TypeError

"""
Keyword-Only Arguments

To specify that a function can have only keyword arguments, add *, before the arguments
"""


def my_function(*, name):
    print("Hello", name)


my_function(name="Emil")
# my_function("Emil")  # This will raise a TypeError


"""
Combining Positional-Only and Keyword-Only

Arguments before / are positional-only, and arguments after * are keyword-only:
"""


def my_function(a, b, /, *, c, d):
    return a + b + c + d


result = my_function(5, 10, c=15, d=20)
print(result)

""" 
*args and **kwargs

By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.
"""

""" 
Arbitrary Arguments - *args

If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly
"""


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

"""
What is *args?

The *args parameter allows a function to accept any number of positional arguments.

Inside the function, args becomes a tuple containing all the passed arguments: 
"""


def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)


my_function("Emil", "Tobias", "Linus")

"""
Using *args with Regular Arguments

You can combine regular parameters with *args.

Regular parameters must come before *args
"""


def my_function(greeting, *names):
    for name in names:
        print(greeting, name)


my_function("Hello", "Emil", "Tobias", "Linus")

"""
Practical Example with *args

*args is useful when you want to create flexible functions:
"""

# Finding the maximum value


def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        max_num = max(max_num, num)
    return max_num


print(my_function(3, 7, 12, 9, 1))

"""
Arbitrary Keyword Arguments - **kwargs

If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly
"""


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

"""
What is **kwargs?

The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments
"""


def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("Sex:", myvar["sex"])
    print("All data:", myvar)


my_function(name="Tobias", age=30, city="Bergen", sex="Male")

""" 
Unpacking Lists with *

If you have values stored in a list, you can use * to unpack them into individual arguments
"""


def my_function(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
result = my_function(*numbers)  # Same as: my_function(1, 2, 3)
print(result)

""" 
Unpacking Dictionaries with **

If you have keyword arguments stored in a dictionary, you can use ** to unpack them
"""


def my_function(fname, lname):
    print("Hello", fname, lname)


person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)  # Same as: my_function(fname="Emil", lname="Refsnes")

""" 
Nonlocal Keyword

The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.
"""


def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x  # With nonlocal, it returns "hello", without it, it returns "Jane"
        x = "hello"

    myfunc2()
    return x


print(myfunc1())
