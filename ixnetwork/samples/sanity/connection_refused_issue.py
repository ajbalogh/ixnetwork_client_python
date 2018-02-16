import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp, IxnQuery


# run multiple gets and try for connection refused

ixnhttp = IxnHttp('10.36.79.30', rest_port=443)
ixnhttp.auth('admin', 'admin')
ixnhttp.current_session = ixnhttp.create_session()
for i in range(0, 100000):
	state = ixnhttp.get('/traffic').state
	result = IxnQuery(ixnhttp, '/').node('traffic').go()
	print('%s %s %s' % (i, result.traffic.href, state))
ixnhttp.delete_session()


