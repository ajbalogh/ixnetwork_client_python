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

# create management objects
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the current configuration
config_mgmt.new_config()

# export the entire configuration
all_objects_from_root = config_mgmt.export_config()
print(json.dumps(all_objects_from_root, indent=4))

# export a non root node and its children
multiple_objects = config_mgmt.export_config('/availableHardware', descend=True)
print(json.dumps(multiple_objects, indent=4))

# export a single object in the configuration that contains multivalues
single_object = config_mgmt.export_config('/globals/topology/ipv4/arpRate', descend=False)
print(json.dumps(single_object, indent=4))

# export multiple objects to a file
ixnhttp.post('/vport', [{'name': 'abc-%d' % i} for i in range(10)])
config_mgmt.export_config('/vport', descend=False, include_defaults=True, local_filename="c:/temp/vports.json")
