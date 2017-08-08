"""IxNetwork Python Client over HTTP

This module interacts with IxNetwork instances using REST.
It provides low level access to the entire IxNetwork low level hierarchy
using get, post, patch, delete, help methods.
It has auth and session methods to enable use with the newer Linux managed sessions.abs
It also exposes a root object that has an IxnQuery that can be used to retrieve
any object in the hierarchy.
"""


import json
try:import httplib
except:import http.client as httplib
import os
import ssl
try:import urllib2
except:import urllib.request as urllib2
import time
from .IxnQuery import IxnQuery
from .IxnDynAttr import IxnDynAttr


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
        return self._generate_ixn_object(self._send_recv('GET', url, fid=fid))
    
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
        
    def _send_recv(self, method, url, payload=None, fid=None, file_content=None):
        if url.find('/api/v1/sessions') == -1 and self.current_session is not None:
            url = "/api/v1/sessions/%s/ixnetwork%s" % (self.current_session.id, url)
        headers = self._headers
        if self.trace:
            print('%s %s %s' % (int(time.time()), method, url))
        if payload is not None:
            headers['Content-Type'] = 'application/json'
            self._connection.request(method, url, body=json.dumps(payload), headers=headers)
        elif method == 'POST' and fid is not None:
            headers['Content-Type'] = 'application/octet-stream'
            self._connection.request(method, url, body=fid, headers=headers)
        elif method == 'POST' and file_content is not None:
            headers['Content-Type'] = 'application/octet-stream'
            self._connection.request(method, url, body=json.dumps(file_content), headers=headers)
        else:
            self._connection.request(method, url, headers=headers)

        response = self._connection.getresponse()
        if str(response.status).startswith('2') is False:
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

    def _generate_ixn_object(self, result):
        if isinstance(result, list):
            for item in result:
                self._generate_ixn_object(item)
        else:
            if hasattr(result, 'href') is True:
                setattr(result, '_ixnhttp', self)
                result.attributes = lambda: None
                result.operations = lambda: None
                result.query = IxnQuery(self, result.href)
                meta_data = self._get_meta_data(result.href)
                self._move_attributes(meta_data, result)
                self._add_operations(meta_data, result)
                self._add_child_creates(meta_data, result)
                self._process_child_instances(meta_data, result)
        return result                        

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

    def _get_dyn_attrs(self, result):
        dyn_attrs = []
        for attr_name in dir(result.attributes):
            dyn_attr = getattr(result.attributes, attr_name)
            if isinstance(dyn_attr, IxnDynAttr):
                dyn_attrs.append(dyn_attr)
        return dyn_attrs

    def _move_attributes(self, meta_data, result):
        for attribute in meta_data.attributes:
            if hasattr(result, attribute.name):
                value = getattr(result, attribute.name)
                setattr(result.attributes, attribute.name, IxnDynAttr(result._ixnhttp, attribute, value))
                delattr(result, attribute.name)

    def _add_operations(self, meta_data, result):
        def dump_operation():
            print( 'href: %s' % (result.href))
            for dyn_attr in self._get_dyn_attrs(result):
                print("%s: %s" % (dyn_attr.name, dyn_attr.value))
        setattr(result, 'dump', dump_operation)

        if meta_data.remove is True:
            def delete_operation():
                result._ixnhttp.delete(result.href)
            delete_operation.__doc__ = 'Delete this %s object' % (meta_data.name)
            setattr(result, 'delete', delete_operation)
        
        update = False
        for attribute in meta_data.attributes:
            if attribute.readOnly is False:
                update = True
                break
        if update is True:
            def update_operation():
                updates = {}
                for dyn_attr in self._get_dyn_attrs(result):
                    if dyn_attr.is_dirty is True and dyn_attr.is_multivalue is False:
                        updates[dyn_attr.name] = dyn_attr.value
                if len(updates.keys()) > 0:
                    result._ixnhttp.patch(result.href, updates)
            update_operation.__doc__ = 'Update this %s object' % (meta_data.name)
            setattr(result, 'update', update_operation)
            
        if len(self._get_dyn_attrs(result)) > 0:
            def refresh_operation():
                includes = []
                dyn_attrs = self._get_dyn_attrs(result)
                for dyn_attr in dyn_attrs:
                    includes.append(dyn_attr.name)
                url = '%s?includes=%s' % (result.href, ', '.join(includes))
                refreshed_attributes = result._ixnhttp._send_recv('GET', url)
                for dyn_attr in dyn_attrs:
                    dyn_attr._value = getattr(refreshed_attributes, dyn_attr.name)
                return result
            refresh_operation.__doc__ = 'Refresh the attributes of this %s object' % (meta_data.name)
            setattr(result, 'refresh', refresh_operation)
        
        for operation in meta_data.operations:
            operation_name = operation.operation.lower()
            def method_operation(payload=None, operation_name=operation_name):
                if result.href[-1] == '/':
                    url = '%soperations/%s' %(result.href, operation_name)
                else:
                    url = '%s/operations/%s' %(result.href, operation_name)
                return result._ixnhttp.post(url, payload)
            setattr(result.operations, operation_name, method_operation)
            getattr(result.operations, operation_name).__doc__ = operation.description
    
    def _add_child_creates(self, meta_data, result):
        for child in meta_data.children:
            url = '%s/%s' % (result.href, child.name)
            child_meta_data = self._get_meta_data(url)

            if child_meta_data.add is True:
                def create_operation(url=url, count=1, payload=None):
                    if payload is None:
                        payload = []
                        for i in range(0, count):
                            payload.append({})
                    response = result._ixnhttp.post(url, payload)
                    new_objects = []
                    for link in response.links:
                        new_object = result._ixnhttp.get(link.href)
                        new_object.href = link.href
                        self._generate_ixn_object(new_object)
                        new_objects.append(new_object)
                    if len(new_objects) == 1:
                        return new_objects[0]
                    else:
                        return new_objects
                create_operation.__doc__ = 'Create a default %s object' % (child_meta_data.name)
                setattr(result, 'create_%s' % (child_meta_data.name), create_operation)


    def _process_child_instances(self, meta_data, result):
        for child in meta_data.children:
            if hasattr(result, child.name):
                value = getattr(result, child.name)
                self._generate_ixn_object(value)




