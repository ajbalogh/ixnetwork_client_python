import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp


# This sample demonstrates how to create a session on the session managed host

# IxNetwork API Server
# create a session using username and password
ixnhttp = IxnHttp(Config.HOST_IP_ADDRESS, rest_port=Config.HOST_REST_PORT)
ixnhttp.auth('admin', 'admin')
session = ixnhttp.create_session()
session.dump()
