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
    # counter
    ethernet.attributes.mac.value.dump()

    # singleValue
    ethernet.attributes.mac.value.single_value = '00:00:de:ad:be:ef'
    print(ethernet.attributes.mac.value.single_value)
    ethernet.attributes.mac.value.dump()

    # valueList
    ethernet.attributes.mac.value.value_list = ['00:00:de:ad:be:ef', '00:00:fa:ce:fa:ce']
    print(ethernet.attributes.mac.value.value_list)
    ethernet.attributes.mac.value.dump()
