"""IxNetwork Python Client over HTTP

This module interacts with IxNetwork instances using REST.
It provides low level access to the entire IxNetwork low level hierarchy
using get, post, patch, delete, help methods.
It has auth and session methods to enable use with the newer Linux managed sessions.abs
It also exposes a root object that has an IxnQuery that can be used to retrieve
any object in the hierarchy.
"""


import json
try:
    import httplib
except:
    import http.client as httplib
import os
import ssl
try:
    import urllib2
except:
    import urllib.request as urllib2
import time
from ixnetwork.IxnQuery import IxnQuery


class IxnHttp(object):
    """IxNetwork REST session. """
    
    Multivalue = 1
    Vport = 2

    _meta_data = {}

    def __init__(self, hostname, rest_port=80, secure=False, api_key=None):
        """ Setup the http connection parameters to a host

        Args:
            hostname: hostname or ip address
            rest_port: the rest port of the host, default of 80 uses http, 443 uses https
            secure: override to force http or https, True to use https, False to use http, default is False
            api_key: the api key supplied by the web based IxNetwork UI 
        """
        self.current_session = None
        self._root = None
        self._file_mgmt = None
        self._meta_data = {}
        self._headers = {}
        self.trace = False
        if api_key is not None:
            self._headers['X-Api-Key'] = api_key
        baseAddress = hostname + ":" + str(rest_port)
        if rest_port == 443 or secure:
            self._connection = httplib.HTTPSConnection(
                baseAddress, context=ssl._create_unverified_context())
        else:
            self._connection = httplib.HTTPConnection(baseAddress)

    def auth(self, username, password):
        """ Authenticate against the host and port

        Args:
            username: a valid username
            password: a valid password
        
        Returns:
            authentication response
        """
        payload = {
            'username': username,
            'password': password
        }
        auth = self.post('/api/v1/auth/session', payload=payload)
        self._headers['X-Api-Key'] = auth.apiKey
        return auth

    def sessions(self):
        """Get a list of sessions on the server """
        return self.get('/api/v1/sessions')

    def create_session(self):
        """Create and set a new IxNetwork session on the host specified in the constructor """
        body = {
            'applicationType': 'ixnrest'
        }
        session = self.post('/api/v1/sessions', payload=body)
        self.post('/api/v1/sessions/%s/operations/start' % session.id, payload=body)
        self.current_session = self.get('/api/v1/sessions/%s' % session.id)
        return self.current_session

    def delete_session(self):
        """Delete the current_session """
        if self.current_session is None:
            raise Exception('There is no current_session to be deleted')
        body = {
            'applicationType': 'ixnrest'
        }
        if self.current_session.state.lower() == 'active':
            self.post('/api/v1/sessions/%s/operations/stop' % self.current_session.id, payload=body)
        self.delete('/api/v1/sessions/%s' % self.current_session.id, payload=body)
        self.current_session = None
    
    @property
    def root(self):
        if self.current_session is not None and self._root is None:
            self._root = IxnQuery(self, '/').go()
        return self._root

    @property
    def system_info(self):
        """Get IxNetwork information: version, username."""
        if self.current_session is not None:
            query_result = self.root.query \
                .node('globals', properties=['buildNumber', 'username']).go()
            return {
                'buildNumber': query_result.globals.attributes.buildNumber.value,
                'username': query_result.globals.attributes.username.value
            }
        raise Exception('The library must be connected to a session in order to retrieve session information')
    
    @property
    def trace(self):
        """True/False to trace all http commands and responses."""
        return self._trace

    @trace.setter
    def trace(self, value):
        self._trace = value

    def _process_async_response(self, url, response):
        while response.progress != 100:
            if self.trace:
                print('%s %s progress %s' % (int(time.time()), response.url, response.progress))
            time.sleep(4)
            response = self._send_recv('GET', response.url)
        if self.trace:
            print('%s POST COMPLETE %s' % (int(time.time()), url))
        if response.state.upper() != 'SUCCESS':
            raise Exception('%s: %s - %s' % (response.state, response.message, response.result))
        return response

    def get(self, url, fid=None):
        if str(url).find('links=true') == -1:
            if str(url).find('?') == -1:
                url += "?"
            else:
                url += "&"
            url += "links=true"
        return self._send_recv('GET', url, payload=None, fid=fid)
    
    def post(self, url, payload=None, fid=None, file_content=None):
        response = self._send_recv('POST', url, payload, fid, file_content)
        if '/operations/' in url:
            response = self._process_async_response(url, response)
        return response

    def patch(self, url, payload):
        return self._send_recv('PATCH', url, payload)

    def delete(self, url, payload=None):
        return self._send_recv('DELETE', url, payload)

    def help(self, url):
        return self._send_recv('OPTIONS', url)

    def _get_meta_data(self, href):
        pieces = href.split('/')
        meta_url = '/'.join(pieces[0:5])
        for i in range(5, len(pieces)):
            piece = pieces[i]
            if len(piece) > 0 and piece.isdigit() is False:
                meta_url = '%s/%s' % (meta_url, piece)
        if meta_url in IxnHttp._meta_data:
            meta_data = IxnHttp._meta_data[meta_url]
        else:
            meta_data = self.help(meta_url).custom
            IxnHttp._meta_data[meta_url] = meta_data
        return meta_data
        
    def _send_recv(self, method, url, payload=None, fid=None, file_content=None):
        if url.find('/api/v1/sessions') == -1 and self.current_session is not None:
            url = "/api/v1/sessions/%s/ixnetwork%s" % (self.current_session.id, url)
        headers = self._headers.copy()
        if self.trace:
            print('%s %s %s' % (int(time.time()), method, url))
        if payload is not None:
            headers['Content-Type'] = 'application/json'
            self._connection.request(method, url, json.dumps(payload), headers)
        elif method == 'POST' and fid is not None:
            headers['Content-Type'] = 'application/octet-stream'
            if fid.__class__.__name__ == 'BufferedReader':
                headers['Content-Length'] = os.fstat(fid.raw.fileno()).st_size
                self._connection.request(method, url, fid.raw, headers)
            else:                            
                self._connection.request(method, url, fid, headers)
        elif method == 'POST' and file_content is not None:
            headers['Content-Type'] = 'application/octet-stream'
            self._connection.request(method, url, json.dumps(file_content), headers)
        else:
            self._connection.request(method, url, None, headers)

        response = self._connection.getresponse()
        if str(response.status).startswith('3') is True:
            content = response.read()
            return self._send_recv(method, response.getheader('Location'), payload=payload, fid=fid, file_content=file_content)
        elif str(response.status).startswith('2') is False:
            raise Exception(response.read())
        elif method == 'GET' and fid is not None:
            fid.write(response.read())
        else:
            content = response.read()
            if len(content) > 0:
                if isinstance(content, bytes):
                    content = content.decode('utf-8')
                return self._make_lambda(json.loads(content))
            else:
                return None

    def _make_lambda(self, contentObject):
        if isinstance(contentObject, list):
            data_list = []
            for item in contentObject:
                data_item = self._make_lambda(item)
                data_list.append(data_item)
            return data_list
        elif isinstance(contentObject, dict):
            data_object = lambda: None
            for key in contentObject:
                value = contentObject[key]
                if isinstance(value, dict) or isinstance(value, list):
                    value = self._make_lambda(value)
                setattr(data_object, key, value)
            def dump_operation():
                for name in dir(data_object):
                    if name.startswith('__') or name.startswith('func_') or name == 'dump':
                        continue
                    value = getattr(data_object, name)
                    print('%s: %s' % (name, value))
            setattr(data_object, 'dump', dump_operation)
            return data_object
        else:
            return contentObject

    def _get_meta_data(self, href):
        pieces = href.split('/')
        meta_url = '/'.join(pieces[0:5])
        for i in range(5, len(pieces)):
            piece = pieces[i]
            if len(piece) > 0 and piece.isdigit() is False:
                meta_url = '%s/%s' % (meta_url, piece)
        if meta_url in IxnHttp._meta_data:
            meta_data = IxnHttp._meta_data[meta_url]
        else:
            meta_data = self.help(meta_url).custom
            IxnHttp._meta_data[meta_url] = meta_data
        return meta_data


