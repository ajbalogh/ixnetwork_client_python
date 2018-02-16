import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp


# This sample demonstrates how to delete all the sessions on a session managed host

# delete all sessions on the managed host
ixnhttp = IxnHttp(Config.HOST_IP_ADDRESS, rest_port=Config.HOST_REST_PORT)
ixnhttp.auth('admin', 'admin')
for session in ixnhttp.sessions():
    ixnhttp.current_session = session
    ixnhttp.delete_session()
