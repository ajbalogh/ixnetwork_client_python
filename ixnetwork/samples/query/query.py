import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnQuery import IxnQuery


# get an IxnHttp instance using the samples Config object
ixnhttp = Config.get_IxnHttp_instance()

# management objects
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the current configuration
config_mgmt.new_config()

# create two virtual ports using the low level http interface
ixnhttp.post('/vport', [{'name': 'eth-1'}, {'name': 'eth-2'}])

# get all the virtual ports using the query
query_result = IxnQuery(ixnhttp, '/') \
    .node('vport', properties=['*']) \
    .go()

# using the returned query_result print the vport names
print('All virtual port names')
for vport in query_result.vport:
    print(vport.attributes.name.value)

# get the eth-2 virtual port using the query
query_result = IxnQuery(ixnhttp, '/') \
    .node('vport', properties=['*'], where=[{'property': 'name', 'regex': 'eth-2'}]) \
    .go()

# using the returned query_result print the vport names
print('One virtual port name')
for vport in query_result.vport:
    print(vport.attributes.name.value)
