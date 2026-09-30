"""
Frozenset

frozenset is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.

Use the frozenset() constructor to create a frozenset from any iterable.
"""

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
