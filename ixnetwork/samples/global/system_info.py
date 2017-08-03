import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp


# demonstrate the way to get test tool information
ixnhttp = Config.get_IxnHttp_instance()
print(ixnhttp.system_info)

