import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp


class Config(object):
    """Initialization class for all the sample code
    Change the static class variables below to reflect which host to connect to.
    All the samples use the static get_IxnHttp_instance method to retrieve an IxnHttp object.

    :param USE_IXNETWORK_GUI_SESSION: True if the samples will connect to a running
    instance of the IxNetwork GUI. False if the samples will connect to a session
    managed host.

    :param HOST_IP_ADDRESS: the hostname or ip address of the IxNetwork test tool

    :param HOST_REST_PORT: the rest port of the IxNetwork test tool
    """
    USE_IXNETWORK_GUI = True
    HOST_IP_ADDRESS = '127.0.0.1'
    HOST_REST_PORT = 11009
    TRACE_REST_CALLS = False

    @staticmethod    
    def get_IxnHttp_instance(use_gui=None, ip_address=None, rest_port=None, username=None, password=None):
        """Get an instance of an IxnHttp class using the static class variables
        
        :param use_gui: override the static class USE_IXNETWORK_GUI

        :param ip_address: override the static class HOST_IP_ADDRESS

        :param rest_port: override the static class HOST_REST_PORT

        :returns: an instance of the IxnHttp class
        """
        if use_gui is not None:
            Config.USE_IXNETWORK_GUI = use_gui
        if ip_address is not None:
            Config.HOST_IP_ADDRESS = ip_address
        if rest_port is not None:
            Config.HOST_REST_PORT = rest_port
        ixnhttp = IxnHttp(Config.HOST_IP_ADDRESS, rest_port=Config.HOST_REST_PORT)
        if Config.USE_IXNETWORK_GUI:
            ixnhttp.current_session = ixnhttp.sessions()[0]
        else:
            ixnhttp.auth(username, password)
            ixnhttp.create_session()
        ixnhttp.trace = Config.TRACE_REST_CALLS
        return ixnhttp

