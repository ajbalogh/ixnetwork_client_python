""" Base class for auto generated NGPF emulation hosts
"""

from ixnetwork.IxnQuery import IxnQuery
import time


class IxnEmulationHost(object):
    def __init__(self, ixnhttp):
        self._ixnhttp = ixnhttp
        self.session_ids = {}
        self._port_offset = None
        self._port_count = None
        self._sessions_per_port = None

    @property
    def hosts(self):
        emulation_hosts = []
        for key in self.session_ids.keys():
            class_name = None
            for piece in key.split('/')[::-1]:
                if piece.isdigit() is False:
                    class_name = piece
                    break
            emulation_host = IxnQuery(self._ixnhttp, key).node(class_name, properties=['*']).go()
            emulation_hosts.append(emulation_host)
        return emulation_hosts

    def _get_topology(self, vport_name):
        vport_query_result = IxnQuery(self._ixnhttp, '/') \
            .node('vport', properties=['name'], where=[{'property': 'name', 'regex': vport_name}]) \
            .go()
        if len(vport_query_result.vport) == 1:
            vport_href = vport_query_result.vport[0].href
            topology_query_result = self._ixnhttp.root.query.clear() \
                .node('topology', properties=['name', 'vports', 'portCount'], where=[{'property': 'vports', 'regex': vport_href}]) \
                .node('deviceGroup', properties=['multiplier']) \
                .go()
            if len(topology_query_result.topology) == 1:
                topology = topology_query_result.topology[0]
                self._port_offset = topology.attributes.vports.value.index(vport_href) + 1
                self._port_count = topology.attributes.portCount.value
                self._sessions_per_port = topology.deviceGroup[0].attributes.multiplier.value
                return topology
            else:
                raise Exception('virtual port with name of %s does not exist in any topology' % vport_name)
        else:
            raise Exception('virtual port with name of %s does not exist' % vport_name)

    def find(self, host_names, vport_name, parent_host, match_properties):
        self.session_ids = {}
        self._port_offset = None
        self._port_count = None
        self._sessions_per_port = None

        start_host = None
        if vport_name is not None:
            start_host = self._get_topology(vport_name)
        elif parent_host is not None:
            start_host = IxnQuery(self._ixnhttp, list(parent_host.session_ids)[0]).go()
            parent_session_ids = parent_host.session_ids
        else:
            raise Exception('A vport_name or parent_host is required')
        start_host.query.clear()

        host_name_to_get = host_names.pop()
        properties = ['count', 'name']
        for key in match_properties.keys():
            if key not in properties:
                properties.append(key)
        start_host.query.node(host_name_to_get, properties=properties)

        for host_name in host_names:
            if not host_name in start_host.href:
                start_host.query.node(host_name)
        
        host_query_result = start_host.query.go()

        hosts = []
        self._get_host_from_query_result(host_names, host_name_to_get, host_query_result, hosts)
        
        if parent_host is not None:
            for host in hosts:
                for key in parent_session_ids:
                    if host.href.startswith(key):
                        self.session_ids[host.href] = {'name': host.attributes.name.value, 'session_ids': parent_session_ids[key]['session_ids']}
            return

        for host in hosts:
            self.session_ids[host.href] = {'name': host.attributes.name.value, 'session_ids': []}
            if len(match_properties.keys()) == 0:
                start = (self._port_offset - 1) * self._sessions_per_port + 1
                end = start + self._sessions_per_port - 1
                self.session_ids[host.href]['session_ids'] = '%s-%s' % (start, end)
            else:
                for key in match_properties.keys():
                    value = getattr(host.attributes, key)
                    if value.is_multivalue:
                        match = match_properties[key]
                        if isinstance(match, list) is False:
                            match = [match]
                        for session_id in value.get_session_ids(match, self._port_count, self._port_offset):
                            if session_id not in self.session_ids[host.href]:
                                self.session_ids[host.href]['session_ids'].append(session_id)
                    elif value.value == match_properties[key]:
                        # self.session_ids[host.href] = '1-%s' % host.attributes.count.value
                        self.session_ids[host.href]['session_ids'] = range(1, host.attributes.count.value + 1)
                    else:
                        break

        for key in self.session_ids:
            if isinstance(self.session_ids[key], list):
                if len(self.session_ids[key]['session_ids']) == 0:
                    self.session_ids[key]['session_ids'] = None
                # else:
                #     self.session_ids[key] = self._session_ids_to_range(self.session_ids[key])

        return self

    def _session_ids_to_range(self, session_ids):
        session_id_range = ''
        start = None
        for current in session_ids:
            if start is None:
                start = previous = current
                continue
            if current == previous + 1:
                previous = current
            else:
                session_id_range += self._build_range(start, previous)
                start = previous = current
        session_id_range += self._build_range(start, previous)
        return session_id_range
    
    def _build_range(self, start, previous):
        if start == previous:
            return '%s;' % start
        else:
            return '%s-%s;' % (start, previous)

    def _get_host_from_query_result(self, parent_names, host_name, query_result, hosts):
        if isinstance(query_result, list):
            for instance in query_result:
                self._get_host_from_query_result(parent_names, host_name, instance, hosts)
        else:
            for attr_name in dir(query_result):
                if attr_name in parent_names:
                    self._get_host_from_query_result(parent_names, host_name, getattr(query_result, attr_name), hosts)
                elif attr_name == host_name:
                    items = getattr(query_result, attr_name)
                    if isinstance(items, list):
                        for item in items:
                            hosts.append(item)
                    else:
                        hosts.append(items)

    def _check_global_topology_status(self, timeout=120):
        start = int(time.time())
        while True:
            global_topology = self._ixnhttp.get('/globals/topology?includes=status')
            if global_topology.status not in ['starting', 'stopping']:
                break
            elif int(time.time()) - start > timeout:
                raise Exception('after %s seconds global topology status is still at %s' % (timeout, global_topology.status))

    def call_operation(self, operation_name, expected_state, timeout):
        self._check_global_topology_status()

        for key in self.session_ids.keys():
            url = '%s/operations/%s' % (key, operation_name)
            self._ixnhttp.post(url, payload={'arg1': [key], 'arg2': self.session_ids[key]['session_ids']})
        
        self.wait_until(expected_state, timeout)

    def wait_until(self, expected_state, timeout=90):
        """Wait until all the sessions in this object are at the expected_state.
        If the wait time exceeds the timeout in seconds throw an exception.
        """
        metadata = None
        for key in self.session_ids.keys():
            if metadata is None:
                metadata = self._ixnhttp.help(key)
                break

        for attribute in metadata.custom.attributes:
            if attribute.type.name == 'list' and attribute.type.innerType.name == 'enum':
                if expected_state in attribute.type.innerType.enums:
                    start = int(time.time())
                    while True:
                        if int(time.time()) - start > timeout:
                            raise Exception('%s host did not reach state %s in %s seconds' % (self.__class__.__name__, expected_state, timeout))
                        states = []
                        for key in self.session_ids.keys():
                            states.append(self._is_at_state(key, attribute.name, self.session_ids[key]['session_ids'], expected_state))
                        if False in states:
                            time.sleep(2)
                        else:
                            self._check_global_topology_status()
                            return 
        raise Exception('%s is not an expected state for this class' % expected_state)
        
    def _is_at_state(self, state_href, state_name, session_ids, expected_state):
        result = self._ixnhttp.get('%s?includes=%s' % (state_href, state_name))
        expected_states = getattr(result, state_name)
        if isinstance(session_ids, str):
            session_index_start = (self._port_offset - 1) * self._sessions_per_port
            session_index_stop = session_index_start + self._sessions_per_port
            for session_index in range(session_index_start, session_index_stop): 
                if expected_states[session_index] != expected_state:
                    return False
        else:
            for session_id in session_ids:
                if expected_states[session_id - 1] != expected_state:
                    return False
        return True     

