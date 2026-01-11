"""Dictionaries are a mutable ordered data type:
 - data in a dictionary consists of key–value pairs;
 - values are accessed by key, not by index as in lists;
 - data in a dictionary is ordered by the order in which elements are added;
 - since dictionaries are mutable, their elements can be changed, added, and removed;
 - a key must be an object of an immutable type: a number, a string, or a tuple; 
 - a value can be data of any type.
"""

routers = {'name': 'R1', 'location': 'New York', 'vendor': 'Cisco'}

# or we can type like this:
routers = {'name': 'R1', 
           'location': 'New York', 
           'vendor': 'Cisco'
           }

# "name", "location", "vendor" are keys of dictionary
# "R1", "New York", "Cisco" are values of dictionary

print(routers["name"])
print(routers["location"])

# to add new key/value pair
routers['ip_address'] = "1.1.1.1"
print(routers)

# as the value, we can use dictionary
routers = {
    'r1': {
        'hostname': 'r1_router',
        'location': 'New York',
        'vendor': 'Cisco',
        'ip': '10.255.0.1'
    },
    'r2': {
        'hostname': 'r2_router',
        'location': 'UAE',
        'vendor': 'Cisco',
        'ip': '10.255.0.2'
    },
    'r3': {
        'hostname': 'r3_router',
        'location': 'London',
        'vendor': 'Juniper',
        'ip': '10.255.0.3'
    },
}

print(routers['r1'])
print(routers['r1']['ip'])

################# Useful methods working with Dictionary

# clear() method. Clears the dictionary
router = {'name': 'r1', 'location': 'New York'}
print(router)
router.clear()
print(router)


# copy() method
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
london2 = london
print(id(london))
print(id(london2))

london['vendor'] = 'Juniper'
print(london2['vendor'])


london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
london2 = london.copy()
print(id(london))
print(id(london2))

london['vendor'] = 'Juniper'
print(london2['vendor'])


# get() method. If a key that does not exist in the dictionary is specified when accessing the dictionary, an error occurs:
device = {'name': 'R1', 'location': 'Tashkent', 'vendor': 'Cisco'}
print(device)
print(device['ip_address'])

print(device.get('ip_address'))
print(device.get('ip_address', 'IP address not found'))

# keys, values, items
device = {'name': 'R1', 'location': 'Tashkent', 'vendor': 'Cisco'}
print(device.keys())
print(device.values())
print(device.items())

# del(). Deletes key and value.
device = {'name': 'R1', 'location': 'Tashkent', 'vendor': 'Cisco'}
del device['name']
print(device)

# update(). This method allows to dict values of other dict
device = {'name': 'R1', 'location': 'Tashkent', 'vendor': 'Cisco'}
device.update({'ip_address': '1.1.1.1', 'os_version': 'Cisco XE'})
print(device)

device.update({'ip_address': '2.2.2.2'}) # update value
print(device)

# How to create a dictionary:
# 1. Create dictionary using literal
 r1 = {'model': 'cisco', 'ios': '15.4'}
print(type(r1))
print(r1)

 # 2. using dict constructor
 r2 = dict([('model', '4451'), ('ios', '15.4')])
print(type(r2))
print(r2)

