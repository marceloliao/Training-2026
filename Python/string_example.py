"""
Quotes Inside Quotes

You can use quotes inside a string, as long as they don't match the quotes 
surrounding the string:
"""

print("He said, \"What's there?\""  + "I said, \"Nothing\"")
print('He said, "What\'s there?"'  + 'I said, "Nothing"')
print('He said, "What\'s there?"'  + 'I said, "Nothing"')

"""
Single or Double Quotes?

String literals can be surrounded by either single quotes or double quotes:
"""

print("Hello")
print('Hello')

"""
Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

for x in "banana":
    print(x)

print("Length of 'strawberry' is", len("strawberry"))

"""
Check String
To check if a certain phrase or character is present in a string, we can use the keyword 'in'.
"""

text = "The best things in life are free!"
print("free" in text)

"""
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in'.
"""

text = "The best things in life are free!"
print("expensive" not in text)
