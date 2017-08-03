from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
import json

# Standalone IxNetwork GUI
# connect to a session with ReST port 12345
ixnetwork_gui = IxnHttp('10.200.22.48', 12345)
ixnetwork_gui.current_session = ixnetwork_gui.sessions()[0]

# management objects
config_mgmt = IxnConfigManagement(ixnetwork_gui)

# clear the current configuration
config_mgmt.new_config()

# export the default configuration
json_config = config_mgmt.export_config()

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

