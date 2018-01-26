"""A high level class that simplifies emulated protocol hosts.

    Example: find all bgp sessions that are up and flap them
    protocol_mgmt = IxnProtocolManagement(ixnhttp)
	bgp_ipv4_peer = protocol_mgmt.find(type='bgpipv4peer', name='BGP Peer 1', session_state='up')
	bgp_ipv4_peer.

"""
from ixnetwork.IxnQuery import IxnQuery


class IxnProtocolManagement(object):
    """Manage emulated protocol hosts"""

    def __init__(self, ixnhttp):
        self._ixnhttp = ixnhttp

	def find(self, type, name, **kwargs):
		""" Find emulated protocol host objects.

		type: the node type
			see the IxNetwork API Doc Browser for all possible node names under /topology
		name: the node name (the content of the name property for the node type)
		**kwargs: remaining search criteria of name/value pairs
			each pair is a node property name/node property value
			see the IxNetwork API Doc Browser for all possible property names for a given node name
			'address', '1.1.1.1', 'gatewayIp', '^(1.1.2.)'

		returns: an IxnNgpfObject that matches the supplied find critieria or None
			the IxnNgpfObject has operations that are specific to the matched sessions
				if only a single session is matched then operations will only be executed against that session
			the base IxnObject is available to allow for modifying the entire node
		"""
		pass
