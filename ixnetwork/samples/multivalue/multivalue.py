import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnMultivalue import IxnMultivalue


# get an IxnHttp instance using the samples Config object
ixnhttp = Config.get_IxnHttp_instance()

# management objects
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the current configuration
config_mgmt.new_config()

# create an ethernet emulation host
ethernet = ixnhttp.root.create_topology().create_deviceGroup().create_ethernet()

# the ethernet mac multivalue object
if ethernet.attributes.mac.is_multivalue:
    ethernet.attributes.mac.value.dump()
    ethernet.attributes.mac.value.single_value = '00:00:de:ad:be:ef'
    ethernet.attributes.mac.value.dump()
