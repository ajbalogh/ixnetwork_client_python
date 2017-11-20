import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnEmulationHosts import IxnIgmpHostEmulation, IxnIpv4Emulation
import os
import time
import json

""" Sample to demonstrate IxnEmulationHosts.py module find method functionality

Load a configuration and find specific sessions for different protocol emulations

"""

# connect to an existing session
ixnhttp = IxnHttp('10.200.22.48', rest_port=12345)
ixnhttp.trace = True
ixnhttp.current_session = ixnhttp.sessions()[0]


# load a binary configuration
config_mgmt = IxnConfigManagement(ixnhttp)
config_mgmt.new_config()


# scaffold
vport = ixnhttp.root.create_child('vport')
ixnhttp.root \
    .create_child('topology', payload={'vports': [vport.href]}) \
    .create_child('deviceGroup', payload={'multiplier': 1}) \
    .create_child('ethernet') \
    .create_child('ipv4')


# find ipv4 emulation host session(s) by vport_name 
ipv4 = IxnIpv4Emulation(ixnhttp)
ipv4.find(vport_name='Ethernet - 001')
print(ipv4.session_ids)


# wait for ipv4 and igmp emulation sessions to be in an up state
ipv4.wait_until(IxnIpv4Emulation.STATE_UP, timeout=10)

