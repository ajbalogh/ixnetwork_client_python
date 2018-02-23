import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.IxnHttp import IxnHttp, IxnQuery


# run multiple gets and try for connection refused

# ixnhttp = IxnHttp('10.36.79.30', rest_port=443)
# ixnhttp.auth('admin', 'admin')
# ixnhttp.current_session = ixnhttp.create_session()
ixnhttp = IxnHttp('127.0.0.1', rest_port=11009)
ixnhttp.current_session = ixnhttp.sessions()[0]
for i in range(0, 100000):
	state = ixnhttp.get('/traffic').state
	# result = IxnQuery(ixnhttp, '/').node('traffic').go()
	print('%s %s' % (i, state))
ixnhttp.delete_session()


