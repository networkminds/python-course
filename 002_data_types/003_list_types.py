"""A list in Python is:
   - a sequence of elements(values) separated by commas and enclosed in square brackets;
   - a mutable ordered data type. 
  
!!! mutable == changeable
"""

list1 = [10,20,30,77]
list2 = ['test', 'test2', 'router']
list3 = [771, 100, 4.0, 'router']

# How to create list:
# 1. Create list using literal
vlans = [100,200,1000,4001]
print(type(vlans))

# 2. Create list using list()
vlan_2 = list("100")
print(vlan_2)
print(type(vlan_2))


router_models = ['cisco','huawei','juniper','acme']
print(router_models[0])
print(router_models[-1])
print(router_models[1:])

# reverse method
vlans = ['10', '15', '20', '30', '100-200']
vlans.reverse()
print(vlans)

# change list values
router_models = ['cisco','huawei','juniper','acme']
router_models[0] = 'mikrotik'
print(router_models)

# list in list
interfaces = [['FastEthernet0/0', '1.1.1.1', 'YES', 'manual', 'up', 'up'],
              ['FastEthernet0/1', '2.2.2.2', 'YES', 'manual', 'up', 'up'],
              ['FastEthernet0/2', '3.3.3.3', 'YES', 'manual', 'up', 'down']
              ]

print(interfaces)
print(interfaces[0])

# len() function returns number of elements inside a list
print(len(interfaces))

# sorted() function. Sorts elements inelements of a list in ascending order and returns a new list with the sorted elements.
routers = ['ZTE', 'Junipoer', 'Acme']
sorted_routers = sorted(routers)
print(sorted_routers)

################# Useful methods working with List
# append(). The append() method adds the specified element to the end of the list.
routers = ['ZTE', 'Junipoer', 'Acme']
routers.append('dlink')
print(routers)

# append() methods changes list on fly and will not return anything. If we want to print we must do in seperate lines
print(routers.append('test_router'))


# extend(). Two add two lists, we can use either extend method or "+" operation
vlans = ['10', '20', '30', '100-200']
vlans2 = ['300', '400', '500']

vlans.extend(vlans2)
print(vlans)

new_vlans = vlans + vlans2
print(new_vlans)


# pop() method. The pop() method removes the element at the specified index. What is important, however, is that the method returns this element.
vlans = ['1', '2', '3', '500-600']
vlans.pop(-1)
vlans.pop(0)

vlans.pop() # deletes last index value and returns deleted result value to the screen

# remove() method deletes selected value
vlans = ['10', '20', '30', '100-200']
vlans.remove('20')


# index() method. Using this method we can find in which index the searched value locates
vlans = ['10', '20', '30', '100-200']
vlans.index('30')

# insert() method. Using this method we can add new values to the list after entered index number
vlans = ['10', '20', '30', '100-200']
vlans.insert(1, '15')


# sort() method. Sorts list on flight
vlans = [1, 50, 10, 15]
vlans.sort()

# count() method. Returns how many times appear this value inside list
vlans = [1, 50, 10, 15, 15]
print(vlans.count(15))