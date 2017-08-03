import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
import json

# get an IxnHttp instance using the samples Config object
ixnhttp = Config.get_IxnHttp_instance()
ixnhttp.trace = True

# create management objects
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the configuration
config_mgmt.new_config()

# export the configuration
ixnhttp.post('/vport', [{'name': 'abc-%d' % i} for i in range(10)])
json_config = config_mgmt.export_config(include_defaults=False)

# import the whole config
for timing in config_mgmt.import_config(json_config).result:
    print(timing)

# modify part of the configuration
json_config['globals']['preferences']['rebootPortsOnConnect'] = True

# configure using the modified configuration fragment
config_mgmt.configure(json_config['globals']['preferences'])

# configure using a fragment
# if there are not 4 vports then they will be created
config_mgmt.configure({'xpath': '/vport[4]'})

# configure the first vport
config_mgmt.configure({'xpath': '/vport[1]', 'name': 'My Virtual Port', 'type': 'ethernetvm'})

# configure the first traffic item
config_mgmt.configure({'xpath': '/traffic/trafficItem[1]', 'name': 'My Traffic Item'})

# configure a multivalue as a singlevalue
fragment = {
    "xpath": "/multivalue[source = '/globals/topology/ospfv3Router/startRate interval']/singleValue",
    "value": "22"
}
config_mgmt.configure(fragment)

