# Strings in python

# String examle
config_template = """
router bgp 1
network 1.1.1.0 mask 255.255.255.0
network 2.2.2.0 mask 255.255.255.0
bgp router-id 1.1.1.1
"""

router_model = "Cisco"

print(config_template)
print(router_model)


# Add strings
interface = "interface"
interface_type = "tunnel0"


ipsec_tunnel = interface + " " + interface_type
print(type(ipsec_tunnel))
print(ipsec_tunnel)

# Access strings using index. Index starts with "0"
print(ipsec_tunnel[0])
print(ipsec_tunnel[-1])
print(ipsec_tunnel[5:])
print(ipsec_tunnel[1:7])
print(ipsec_tunnel[-3:])

# to get all even numbers
even_numbers = "0123456789"
print(even_numbers[::2])

# len() method returns length of string
print(len(ipsec_tunnel))

################# Useful methods working with Strings
# join method
vlans = ['10','20','30']
formatted_vlan = ",".join(vlans)

print(formatted_vlan)

# upper, lower, swapcase, capitalize methods
interface = "FastEthernet"
print(interface.upper())
print(interface.lower())
print(interface.swapcase())

tunnel = "tunnel1"
print(tunnel.capitalize())


# count method. Returns how many times symbol or string appeared in the string 
string1 = 'tunnel0, tunnel1, tunnel2, tunnel0'
print(string1.count('tunnel0'))

# find method. 
string1 = 'interface FastEthernet0/0'
print(string1.find('Fast'))

string2 = string1[string1.find('Fast')::]
print(string2)

# startswith, endswith methods
interface_type = 'FastEthernet0/1'
print(interface_type.startswith('Fast'))
print(interface_type.startswith('fast'))

print(interface_type.endswith('0/1'))

# replace method
string1 = 'FastEthernet0/1'
string1.replace('Fast', 'Gigabit')

# strip method. By default strip method deletes only "space" symbols (\t\n\r\f\v)
string1 = '\n\tinterface FastEthernet0/1\n'
print(string1)
print(string1.strip())

ospf_metric = '[110/1045]'
print(ospf_metric.strip('[]'))

ospf_metric = '[110/1045]'
print(ospf_metric.lstrip('['))
print(ospf_metric.rstrip(']'))


# split method. The split() method splits a string into parts using a character 
# (or characters) as a delimiter and returns a list of strings.
port_template = 'switchport trunk allowed vlan 771,100,20,100-200'
interface_params = port_template.split()
print(interface_params)
print(type(interface_params))

vlans = interface_params[-1]
only_vlans = vlans.split(',')
print(only_vlans)


sh_ip_int_br = "FastEthernet0/0       15.0.15.1    YES manual up         up"
print(sh_ip_int_br.split())


# Formatting strings
interface = "interface FastEthernet0/{}".format('1')
print(interface)

bgp_template = """
router bgp {as_number}
network {subnet} {mask}
"""

bgp_cmd = bgp_template.format(as_number="65100",subnet="1.1.1.0", mask="255.255.255.0")
print(bgp_cmd)