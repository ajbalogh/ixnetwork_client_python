import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp, IxnQuery
from ixnetwork.IxnConfigManagement import IxnConfigManagement


# get an IxnHttp instance using the samples Config object
ixnhttp = Config.get_IxnHttp_instance()

# management objects
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the current configuration
config_mgmt.new_config()

# create two virtual ports
vports = ixnhttp.root.create_child('vport', count=2)

# setup topology west
w_ipv4 = ixnhttp.root.create_child('topology', payload={'vports': [vports[0].href]}) \
    .create_child('deviceGroup').create_child('ethernet').create_child('ipv4')

# setup topology east
e_ipv4 = ixnhttp.root.create_child('topology', payload={'vports': [vports[1].href]}) \
    .create_child('deviceGroup').create_child('ethernet').create_child('ipv4')

# add a traffic item
traffic = ixnhttp.root.query.clear().node('traffic').go().traffic
protocol_templates = traffic.query.node('protocolTemplate', properties=['*'], where=[{'property': 'stackTypeId', 'regex': '^udp$'}]).go().protocolTemplate
traffic_item = traffic.create_child('trafficItem', payload={'trafficType': 'ipv4'})

# add an endpointSet
endpoint_set = traffic_item.create_child('endpointSet', payload={'sources': [w_ipv4.href], 'destinations': [e_ipv4.href]})

# add a stack
config_element = traffic_item.query.node('configElement').node('stack', properties=['*']).go().configElement[0]
stack = config_element.stack[-2]
response = stack.operations.appendprotocol({'arg1': stack.href, 'arg2': protocol_templates[0].href})

# modify a field
field = IxnQuery(ixnhttp, response.result).node('stack', properties=['*']).node('field', properties=['*']).go().field[0]
field.attributes.auto.value = False
field.attributes.valueType.value = 'singleValue'
field.attributes.singleValue.value = '234'
field.update()

