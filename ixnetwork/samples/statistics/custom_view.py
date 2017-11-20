import os, sys, time, traceback

from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement
from ixnetwork.IxnPortManagement import IxnPortManagement
from ixnetwork.IxnStatManagement import IxnStatManagement
from ixnetwork.IxnQuery import IxnQuery

# load a configuration in the gui, assign ports, start protocols, start traffic
# then run this script to create a custom layer23TrafficFlow view
ixnhttp = IxnHttp('10.200.22.48', rest_port=12345)
ixnhttp.current_session = ixnhttp.sessions()[0]

# get the statistics object
query_result = IxnQuery(ixnhttp, '/').node('statistics').go()

# create a view
custom_view_caption = "A Custom View"
payload = {
    'caption': custom_view_caption,
    'type': 'layer23TrafficFlow',
    'visible': True
}
custom_view = query_result.statistics.create_child('view', payload=payload)

# create layer23TrafficFlowFilter payload
layer23_traffic_flow_filter = IxnQuery(ixnhttp, custom_view.href) \
	.node('layer23TrafficFlowFilter', properties=['*']) \
	.go().layer23TrafficFlowFilter

# add port filter names to the payload
query_result = IxnQuery(ixnhttp, custom_view.href).node('availablePortFilter', properties=['name']).go()
hrefs = []
for port_filter in query_result.availablePortFilter:
	hrefs.append(port_filter.href)
layer23_traffic_flow_filter.attributes.portFilterIds.value = hrefs

# add traffic item filter names to the payload
query_result = IxnQuery(ixnhttp, custom_view.href).node('availableTrafficItemFilter', properties=['name']).go()
hrefs = []
for traffic_filter in query_result.availableTrafficItemFilter:
	hrefs.append(traffic_filter.href)
layer23_traffic_flow_filter.attributes.trafficItemFilterIds.value = hrefs

# update the filter
layer23_traffic_flow_filter.update()

# enable the stats column to be displayed
query_result = IxnQuery(ixnhttp, custom_view.href).node('statistic', properties=['*']).go()
for statistic in query_result.statistic:
    statistic.attributes.enabled.value = True
    statistic.update()

# enable the custom view
custom_view.attributes.enabled.value = True
custom_view.update()

# print the statistics
stat_mgmt = IxnStatManagement(ixnhttp)
view_page = stat_mgmt.get_view_page(custom_view_caption)
stat_mgmt.print_view_page(view_page)
