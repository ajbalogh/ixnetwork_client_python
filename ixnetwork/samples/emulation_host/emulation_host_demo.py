import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnPortManagement import IxnPortManagement
from ixnetwork.IxnStatManagement import IxnStatManagement
from ixnetwork.IxnEmulationHosts import IxnIgmpHostEmulation, IxnIpv4Emulation
import os
import time
import json


# connect to an existing session
ixnhttp = IxnHttp('10.200.22.48', rest_port=12345)
ixnhttp.current_session = ixnhttp.sessions()[0]


# print system information
print(ixnhttp.system_info)


# load a binary configuration
config_mgmt = IxnConfigManagement(ixnhttp)
config_filename = '%s/emulation-host-demo.ixncfg' % os.path.dirname(os.path.realpath(__file__))
config_mgmt.load_config(config_filename, upload=True, remove_chassis=True)


# get a list of vports and change the type to ethernet
query_result = ixnhttp.root.query \
    .node('vport', properties=['type', 'connectedTo']) \
    .go()
for vport in query_result.vport:
    vport.operations.unassignports({'arg1': [vport.href], 'arg2': False})
    vport.attributes.type.value = 'ethernet'
    vport.attributes.connectedTo.value = 'null'
    vport.update()


# assign hardware ports to virtual ports
port_mgmt = IxnPortManagement(ixnhttp)
port_mgmt.map('PE2-6/5', '10.200.109.21', '1', '3') \
    .map('PE2-6/8', '10.200.109.21', '1', '4') \
    .apply()


# find igmp emulation host session(s) by vport_name and mac addresses
igmp = IxnIgmpHostEmulation(ixnhttp)
igmp.find(vport_name='PE2-6/5', versionType='version2')
print(igmp.session_ids)


# find ipv4 emulation host session(s) by vport_name 
ipv4 = IxnIpv4Emulation(ixnhttp)
ipv4.find(vport_name='PE2-6/8')
print(ipv4.session_ids)


# low level API start all protocols
ixnhttp.root.operations.startallprotocols()


# wait for ipv4 and igmp emulation sessions to be in an up state
ipv4.wait_until(IxnIpv4Emulation.STATE_UP, timeout=90)
igmp.wait_until(IxnIgmpHostEmulation.STATE_UP, timeout=90)


# stop the ipv4 and igmp emulation sessions
igmp.stop(IxnIgmpHostEmulation.STATE_NOTSTARTED, timeout=90)
ipv4.stop(IxnIpv4Emulation.STATE_NOTSTARTED, timeout=90)


# print statistics
time.sleep(5)
stat_mgmt = IxnStatManagement(ixnhttp)
views = stat_mgmt.get_views()
print(views)
port_summary_page = stat_mgmt.get_view_page('Port Summary')
stat_mgmt.print_view_page(port_summary_page, column_captions=[
    'Port', 'Sessions Total', 'Sessions Up', 'Sessions Down', 'Sessions Not Started'])
protocols_summary_page = stat_mgmt.get_view_page('Protocols Summary')
stat_mgmt.print_view_page(protocols_summary_page, column_captions=[
    'Protocol Type', 'Sessions Total', 'Sessions Up', 'Sessions Down', 'Sessions Not Started'])

