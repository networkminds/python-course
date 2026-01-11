"""
A tuple in Python is:
- a sequence of elements separated by commas and enclosed in parentheses;
- an immutable ordered data type.

!!! immutable == unchangeable

Briefly speaking, tuple is a list with only read access. We cannot change (update, delete) any values inside a tuple.
tuple - кортеж
"""

# create a free tuple
tuple1 = tuple()
print(type(tuple1))

# tuple with a single element
router = tuple("r1",)
print(type(router))
print(type(router))

# tuple from a list
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
tuple_keys = tuple(list_keys)
print(tuple_keys)

print(tuple_keys[0])

# try to change value in a tuple()
tuple_keys[0] = "test_data"

sorted(tuple_keys)
print(tuple_keys)