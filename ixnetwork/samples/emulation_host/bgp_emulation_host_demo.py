import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnPortManagement import IxnPortManagement
from ixnetwork.IxnStatManagement import IxnStatManagement
from ixnetwork.IxnEmulationHosts import IxnBgpIpv4PeerEmulation, IxnIpv4PrefixPoolsEmulation
import os
import time
import json


# connect to an existing session
ixnhttp = IxnHttp('10.200.22.48', rest_port=12345)
ixnhttp.current_session = ixnhttp.sessions()[0]


# load a binary configuration
config_mgmt = IxnConfigManagement(ixnhttp)
config_filename = '%s/bgp-emulation-host-demo.ixncfg' % os.path.dirname(os.path.realpath(__file__))
config_mgmt.load_config(config_filename, upload=True, remove_chassis=True)


# find bgp emulation host session(s) by vport_name
bgpv4 = IxnBgpIpv4PeerEmulation(ixnhttp)
bgpv4.find(vport_name='Ethernet - 001')
print(bgpv4.session_ids)


# find ipv4 prefix pools emulation host session(s) by vport_name
v4pool = IxnIpv4PrefixPoolsEmulation(ixnhttp)
v4pool.find(vport_name='Ethernet - 001')
print(v4pool.session_ids)


# adjust ipv4 prefix pool attributes
v4pool.hosts[0].attributes.networkAddress.value.single_value = '1.1.1.1'
v4pool.hosts[0].attributes.networkAddress.value.set_overlay(1, '1.2.1.1')