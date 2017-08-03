# from IxnHttp import IxnHttp
import json


class IxnPortManagement(object):
    """A high level class that simplifies the process of mapping virtual ports to physical ports

        Example:
        port_mgmt = IxnPortManagement(ixnhttp)
        port_mgmt \
            .map('Ethernet - 001', '10.200.109.3', '1', '1') \
            .map('Ethernet - 002', '10.200.109.3', '1', '2') \
            .apply()
    """

    def __init__(self, ixnhttp):
        self._ixnhttp = ixnhttp
        self.clear()

    def clear(self):
        """Clear all internal virtual port to physical port mappings in this object."""
        self._payload = {
            'arg1': [],
            'arg2': [],
            'arg3': [],
            'arg4': True
        }

    def map(self, vport_name, chassis_ip, card_id, port_id):
        """Add a map of a virtual port to an Ixia port using the virtual ports name"""
        self._ixnhttp.root.query.clear()
        query_result = self._ixnhttp.root.query.node('vport', properties=['name'], where=[{'property': 'name', 'regex': vport_name}]).go()
        if len(query_result.vport) == 1:
            self._payload['arg1'].append({'arg1': chassis_ip, 'arg2': card_id, 'arg3': port_id})
            self._payload['arg3'].append(query_result.vport[0].href)
            return self
        else:
            raise Exception('vport %s does not exist on the server' % vport_name)

    def apply(self):
        """Apply all mappings by executing the assignPorts operation on the test tool"""
        self._ixnhttp.root.operations.assignports(self._payload)

