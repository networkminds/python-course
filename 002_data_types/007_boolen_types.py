"""
Boolean values
- Boolean values in Python are the two constants True and False.

In Python, not only True and False are considered true or false values.
True values:
- any non-zero number
- any non-empty string
- any non-empty object

False values:
0
None
an empty string
an empty object

Other true and false values generally follow logically from the condition.

To check the boolean value of an object, you can use bool():
"""

items = [1, 2, 3]
empty_list = []

print(bool(empty_list))
print(bool(items))

print(bool(0))
print(bool(1))
