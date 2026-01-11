"""
A set is a mutable unordered data type. A set always contains only unique elements.
A set in Python is a sequence of elements separated by commas and enclosed in curly braces.
Using a set, you can easily remove duplicate elements:
"""
vlans = [10, 20, 30, 40, 100, 10]

unique_vlans = set(vlans)
print(unique_vlans)

################# useful methods working with a Set

# add(). This method adds value to the set
vlan = {10,20,30,40}
vlan.add(50)
print(vlan)

# discard(). This method will delete an element from the set. If element not exists it will not generaty error
print(vlan)
vlan.discard(771)

# clear(). This method clears the set
vlan.clear()
print(vlan)

# Sets are useful because you can perform various operations on them and find the union of sets, 
# the intersection, and so on.
# The union of sets can be obtained using the union() method or the | operator.

router1_vlans = {10, 20, 30, 50, 100}
router2_vlans = {100, 101, 102, 200}

result =router1_vlans.union(router2_vlans)
print(result)

print(vlans1 | vlans2)

# You cannot create an empty set using a literal (because in that case it would be a dictionary, not a set):
set1 = {}
print(type(set1))

# create an empty set
set2 = set()
print(type(set2))

# create set from a given list
vlans = ['10', '15', '20', '30', '30','100-200']
unique_vlans = set(vlans)
print(unique_vlans)
