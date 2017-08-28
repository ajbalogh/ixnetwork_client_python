import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnPortManagement import IxnPortManagement


# connect to an existing session
ixnhttp = IxnHttp('10.200.22.48', rest_port=12345)
ixnhttp.current_session = ixnhttp.sessions()[0]

# clear the config
IxnConfigManagement(ixnhttp).new_config()

# add 2 vports
vports = ixnhttp.root.create_vport(count=2)

# map 2 vports to previously created vports
chassis_ip = '10.200.109.3'
port_mgmt = IxnPortManagement(ixnhttp)
port_mgmt.map(vports[0].attributes.name.value, chassis_ip, 1, 1) \
    .map(vports[1].attributes.name.value, chassis_ip, 1, 2)

# map 2 new vports
port_mgmt.map(None, chassis_ip, 1, 3) \
    .map(None, chassis_ip, 1, 4)

# print the current state of all mappings
print(port_mgmt.status())

# apply the mapping on the server
port_mgmt.apply(force_clear_ownership=True)

# print the current state of all mappings
print(port_mgmt.status())

# unapply the mapping on the server
port_mgmt.unapply()

# print the current state of all mappings
print(port_mgmt.status())

    
