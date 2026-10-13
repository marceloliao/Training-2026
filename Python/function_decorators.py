"""
Python Decorators

Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.

"""

# Basic Decorator
# Define the decorator first, then apply it with @decorator_name above the function.


def changecase(func):
    def myinnner():
        return func().upper()

    return myinnner


@changecase  # By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
def myfunction():
    return "Hello World"


print(myfunction())  # Output: Hello World


def changecase(func):
    def myinner(x):
        return func(x).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


"""
*args and **kwargs 

Sometimes the decorator function has no control over the arguments passed from decorated function, 
to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function 
can accept any number, and any type of arguments, and pass them to the decorated function.
"""


def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return myinner


@changecase
def myfunction2(name):
    return "Ola " + name


print(myfunction2("Tim"))

"""
Decorator With Arguments

Decorators can accept their own arguments by adding another wrapper level. 
"""


def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a

        return myinner

    return changecase


@changecase(2)
def myfunction():
    return "Hello Linus"


print(myfunction())

""" 
Multiple Decorators

You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.
"""


def changecase(func):
    def myinner():
        return func().upper()

    return myinner


def addgreeting(func):
    def myinner():
        return "Hello " + func() + ", Have a good day!"

    return myinner


@changecase
@addgreeting
def myfunction():
    return "James"


print(myfunction())

""" 
Preserving Function Metadata

Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
"""


def function_to_return_greeting():
    return "Have a great day!"


print(function_to_return_greeting.__name__)
print(function_to_return_greeting.__doc__)


# But, when a function is decorated, the metadata of the original function is lost.
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)
