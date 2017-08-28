"""A high level class that simplifies the process of
    adding physical ports annd mapping virtual ports to physical ports

    Example:
    port_mgmt = IxnPortManagement(ixnhttp)
	port_mgmt \
        .map('10.200.109.3', '1', '1') \
        .map('10.200.109.3', '1', '2') \
        .map('Ethernet - 001', '10.200.109.3', '1', '3') \
        .map('Ethernet - 002', '10.200.109.3', '1', '4') \
        .apply(force_clear_ownership=True)
	port_mgmt.release()
"""
from ixnetwork.IxnQuery import IxnQuery


class IxnPortManagement(object):
    """Manage virtual port and physical port connections"""

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
        """Map an existing virtual port to a chassis/card/port"""
        if vport_name is None:
            href = self._ixnhttp.root.create_vport().href
        else:
            query_result = IxnQuery(self._ixnhttp, '/').node('vport', properties=['name'], where=[{'property': 'name', 'regex': vport_name}]).go()
            if len(query_result.vport) != 1:
                raise Exception('vport %s does not exist on the server' % vport_name)    
            href = query_result.vport[0].href
        self._payload['arg1'].append({'arg1': chassis_ip, 'arg2': card_id, 'arg3': port_id})
        self._payload['arg3'].append(href)
        return self

    def apply(self, force_clear_ownership=False):
        """Apply all mappings by executing the assignPorts operation on the test tool"""
        self._payload['arg4'] = force_clear_ownership
        self._ixnhttp.root.operations.assignports(self._payload)

    def status(self):
        """Get the status of the mappings"""
        query_result = IxnQuery(self._ixnhttp, '/').node('vport', properties=['name', 'connectionStatus']).go()
        status = []
        for vport in query_result.vport:
            if vport.href in self._payload['arg3']:
                status.append('%s: %s' % (vport.attributes.name.value, vport.attributes.connectionStatus.value))
        return status

    def unapply(self):
        """Unapply all mappings by executing the unassignPorts operation on the test tool"""
        payload = {
            'arg1': self._payload['arg3'],
            'arg2': False
        }
        self._ixnhttp.post('/vport/operations/unassignports', payload)
        