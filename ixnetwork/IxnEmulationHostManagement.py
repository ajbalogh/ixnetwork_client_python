"""A high level class that simplifies emulation host
	session management.

    Example:
    host_mgmt = IxnEmulationHostManagement(ixnhttp)
	ipv4 = host_mgmt.find('ipv4')
	given an ipv4 emulation host do the following:
		set multivalues based on specific sessions
		do operations on specific sessions

"""
from ixnetwork.IxnQuery import IxnQuery


class IxnEmulationHostManagement(object):
    """Manage emulation hosts"""

    def __init__(self, ixnhttp):
        self._ixnhttp = ixnhttp

	def find(self):
		pass
