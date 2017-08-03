import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp


# This sample demonstrates how to connect to a running standalone IxNetwork GUI session

# specify the connection parameters of the target host
# the ReST port is specified in the IxNetwork GUI command line as -restport <tcp port number>
# and can also be found in the log view window under the RestAPIService tab as the first entry 
ixnetwork_gui = IxnHttp(Config.HOST_IP_ADDRESS, rest_port=Config.HOST_REST_PORT)

# get a list of sessions on that ipaddress and rest port
# since this is an IxNetwork GUI there will be only one session
sessions = ixnetwork_gui.sessions()

# print out the details of each session
# there should only be one session
for session in sessions:
    session.dump()

# set the current session to be the one and only session
ixnetwork_gui.current_session = sessions[0]

