import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement


# get an IxnHttp instance using the samples Config object
ixnhttp = Config.get_IxnHttp_instance()

# get the configuration management object
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the current configuration
config_mgmt.new_config()

# create two virtual ports
vports = ixnhttp.root.create_child('vport', count=2)

# create a topology west
# add a vport reference to the topology
# includes a deviceGroup, ethernet, ipv4
w_topology = ixnhttp.root.create_child('topology')
w_topology.attributes.vports.value = [vports[0].href]
w_topology.attributes.name.value = 'West'
w_topology.update()
w_ipv4 = w_topology.create_child('deviceGroup') \
	.create_child('ethernet') \
	.create_child('ipv4')

# change the address and gw multivalue
w_ipv4.attributes.address.value.single_value = '1.1.1.1'
w_ipv4.attributes.gatewayIp.value.single_value = '1.1.1.2'

# create a topology east
# add a vport reference to the topology
# includes a deviceGroup, ethernet, ipv4
e_topology = ixnhttp.root.create_child('topology')
e_topology.attributes.vports.value = [vports[1].href]
e_topology.attributes.name.value = 'East'
e_topology.update()
e_ipv4 = e_topology.create_child('deviceGroup') \
	.create_child('ethernet') \
	.create_child('ipv4')

# change the address and gw multivalue
e_ipv4.attributes.address.value.single_value = '1.1.1.2'
e_ipv4.attributes.gatewayIp.value.single_value = '1.1.1.1'

# create an ipv4 traffic item
traffic = ixnhttp.root.query.clear().node('traffic', properties = ['*']).go().traffic
traffic_item = traffic.create_child('trafficItem', payload = {'trafficType': 'ipv4'})
endpoint_set = traffic_item.create_child('endpointSet', payload = {
	'sources': [w_ipv4.href],
	'destinations': [e_ipv4.href]
	}
)
high_level_streams = traffic_item.query.node('highLevelStream', properties = ['*']).go().highLevelStream
print(high_level_streams)
# adjust frameSize, frameRate, transmissionControl, stack, field
