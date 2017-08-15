""" Sample to demonstrate IxnEmulationHosts.py module find method functionality

Load a configuration and find specific sessions for different protocol emulations

"""
import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnEmulationHosts import IxnEthernetEmulation, IxnIpv4Emulation, IxnIgmpHostEmulation

use_gui = False

if use_gui:
    ixnhttp = IxnHttp('10.200.22.48', rest_port=12345)
    ixnhttp.current_session = ixnhttp.sessions()[0]
else:
    ixnhttp = IxnHttp('10.200.23.60', rest_port=443)
    ixnhttp.trace = True
    ixnhttp.auth('admin', 'admin')
    ixnhttp.create_session()


# load a binary configuration
config_mgmt = IxnConfigManagement(ixnhttp)
config_filename = '%s/emulation-host-demo.ixncfg' % os.path.dirname(os.path.realpath(__file__))
config_mgmt.load_config(config_filename, upload=True, remove_chassis=True)


# find ethernet emulation host session(s) by vport_name or parent 
eth = IxnEthernetEmulation(ixnhttp)
eth.find(vport_name='PE2-6/8')
print(eth.session_ids)

ipv4 = IxnIpv4Emulation(ixnhttp)
ipv4.find(emulation_host=eth)
print(ipv4.session_ids)

igmp = IxnIgmpHostEmulation(ixnhttp)
igmp.find(emulation_host=ipv4)
print(igmp.session_ids)


# cleanup session
if use_gui is False:
    ixnhttp.delete_session()
