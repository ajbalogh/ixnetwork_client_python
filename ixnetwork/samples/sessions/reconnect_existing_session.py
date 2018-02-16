import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp


# this sample demonstrates how to reconnect to an existing session if one exists
ixnhttp = IxnHttp(Config.HOST_IP_ADDRESS, rest_port=Config.HOST_REST_PORT)
ixnhttp.auth('admin', 'admin')
sessions = ixnhttp.sessions()
for session in sessions:
    session.dump()
if len(sessions) > 0:
    ixnhttp.current_session = sessions[0]


