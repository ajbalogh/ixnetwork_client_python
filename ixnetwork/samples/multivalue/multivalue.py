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
ethernet = ixnhttp.root.create_child('topology').create_child('deviceGroup').create_child('ethernet')

# ethernet mac singleValue
ethernet.attributes.mac.value.single_value = '00:00:de:ad:be:ef'
print(ethernet.attributes.mac.value.single_value)
ethernet.attributes.mac.value.dump()

# ethernet mac valueList
ethernet.attributes.mac.value.value_list = ['00:00:de:ad:be:ef', '00:00:fa:ce:fa:ce']
print(ethernet.attributes.mac.value.value_list)
ethernet.attributes.mac.value.dump()

# ethernet enable vlans
ethernet.attributes.vlanCount.value = 3
ethernet.update()
ethernet.attributes.enableVlans.value.single_value = 'true'

# get the vlan emulation host
vlan = ethernet.query.node('vlan', properties=['vlanId', 'priority', 'tpid']).go().vlan[0]

# vlan vlanId singleValue
vlan.attributes.vlanId.value.single_value = '6'
vlan.attributes.vlanId.value.dump()

# vlan vlanId increment counter
vlan.attributes.vlanId.value.set_counter('100', '1', 'increment')
vlan.attributes.vlanId.value.dump()
assert vlan.attributes.vlanId.value.get_values(2, 1)[0] == '102'

# vlan vlanId decrement counter
vlan.attributes.vlanId.value.set_counter('90', '1', 'decrement')
vlan.attributes.vlanId.value.dump()
assert vlan.attributes.vlanId.value.get_values(2, 1)[0] == '88'

# vlan vlanId repeatableRandom 
vlan.attributes.vlanId.value.set_repeatable_random(count=10, fixed=0, mask=6, seed=1)
vlan.attributes.vlanId.value.dump()
assert vlan.attributes.vlanId.value.get_values(2, 1)[0] == '4'

# vlan vlanId repeatableRandomRange 
vlan.attributes.vlanId.value.set_repeatable_random_range(min=1, max=10, step=1, seed=1)
vlan.attributes.vlanId.value.dump()
assert vlan.attributes.vlanId.value.get_values(2, 1)[0] == '10'