import StringIO
import os
from ixnetwork import *


def process_node(ixnhttp, parent_href, metadata, classes):
    """
        ixnhttp: rest access
        parent_href: parent node href
        metadata: child metadata
        classes: repository for newly created classes
    """
    class_name = 'Ixn%s%sEmulation' % (metadata.custom.name[0].upper(), metadata.custom.name[1:])
    href = '%s/%s' % (parent_href, metadata.custom.name)
    node = None
    try:
        node = ixnhttp._send_recv('GET', href)
        if isinstance(node, list):
            if len(node) == 0:
                raise Exception('object does not exist')
            else:
                node = node[0]
                href = node.links[-1].href
    except:        
        try:
            node = ixnhttp._send_recv('POST', href)
            href = node.links[0].href
            node = ixnhttp._send_recv('GET', href)
        except:
            message = '%s failed to GET or POST %s' % (parent_href, metadata.custom.name)
            raise Exception(message)

    if class_name in classes.keys():
        return href

    # build find
    expected_states = []
    attr_doc_string = '%s"""Find specific %s emulated host sessions using a virtual port name or a parent emulation host and optional filters.\n' % (' ' * 8, metadata.custom.name)
    attr_doc_string += '%sFilter values can be a single value or a list of values, see the specific **filter information below.\n\n' % (' ' * 12)
    attr_doc_string += '%svport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)\n' % (' ' * 12)
    attr_doc_string += '%semulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)\n' % (' ' * 12)
    attr_doc_string += '%s**filters:\n' % (' ' * 12)
    for attribute in metadata.custom.attributes:
        if attribute.deprecated is False:
            type_name = attribute.type.name
            attr_written = True
            if type_name == 'href' and 'multivalue' in attribute.type.hrefs[0]:
                multivalue_href = getattr(node, attribute.name)
                multivalue = ixnhttp.get(multivalue_href)
                if len(multivalue.enums) > 0:
                    attr_doc_string += '%s%s: string (string type: enum  enums: %s)' % (' ' * 16, attribute.name, '|'.join(multivalue.enums))
                else:
                    attr_doc_string += '%s%s: string | list[string] (string type: %s)' % (' ' * 16, attribute.name, multivalue.format)
            elif type_name == 'object':
                continue
            elif type_name == 'list' and attribute.type.innerType.name == 'enum':
                expected_states = attribute.type.innerType.enums
                attr_written = False
            elif type_name == 'enum':
                attr_doc_string += '%s%s: string (string type: enum  enums: %s)' % (' ' * 16, attribute.name, '|'.join(attribute.type.enums))
            else:
                attr_doc_string += '%s%s: %s' % (' ' * 16, attribute.name, attribute.type.name)
            if attr_written is True:
                attr_doc_string += '\n'
    attr_doc_string += '%s"""\n' % (' ' * 8)

    if len(expected_states) == 0:
        return href

    fid = StringIO.StringIO()

    # write class and __init__
    fid.write('class %s(IxnEmulationHost):\n' % (class_name))
    fid.write('%s"""Generated NGPF %s emulation host """\n' % (' ' * 4, metadata.custom.name))
    fid.write('\n')
    for expected_state in expected_states:
        fid.write('%sSTATE_%s = \'%s\'\n' % (' ' * 4, expected_state.upper(), expected_state))
    fid.write('\n')
    fid.write('%sdef __init__(self, ixnhttp):\n' % (' ' * 4))
    fid.write('%ssuper(%s, self).__init__(ixnhttp)\n' % (' ' * 8, class_name))
    fid.write('\n')

    # write find
    class_names = metadata.custom.path.split('/')[1:]
    class_names = ','.join('"{0}"'.format(class_name) for class_name in class_names)
    fid.write('%sdef find(self, vport_name=None, emulation_host=None, **filters):\n' %  (' ' * 4))
    fid.write(attr_doc_string)
    fid.write('%sreturn super(%s, self).find([%s], vport_name, emulation_host, filters)\n' % (' ' * 8, class_name, class_names))
    fid.write('\n')

    # write operations
    for operation in metadata.custom.operations:
        if len(operation.args) == 2 and operation.args[1].type.name == 'string':
            fid.write('%sdef %s(self, expected_state=None, timeout=None):\n' % (' ' * 4, operation.operation.lower()))
            fid.write('%s"""%s\n' % (' ' * 8, ' '.join(operation.description.split())))
            fid.write('%sFor expected_state options see the class state variables\n' % (' ' * 12))
            fid.write('%s"""\n' % (' ' * 8))
            fid.write('%ssuper(%s, self).call_operation(\'%s\', expected_state, timeout)\n' % (' ' * 8, class_name, operation.operation))
            fid.write('\n')
    fid.write('\n')

    classes[class_name] = fid.getvalue()
    fid.close()
    print('GENERATED: %s' % class_name)
    return href

def process_query_result(ixnhttp, query_result, classes):
    if query_result is None:
        return
    metadata = ixnhttp.help(query_result.href)
    for child in metadata.custom.children:
        if child.name in ['port', 'item'] or hasattr(query_result, child.name) is False:
            continue
        attr = getattr(query_result, child.name)
        if isinstance(attr, list) is True:
            if len(attr) == 0:
                continue
            else:
                attr = attr[0]
        href = query_result.href
        metadata = ixnhttp.help('%s/%s' % (href, child.name))
        process_node(ixnhttp, href, metadata, classes)
        process_query_result(ixnhttp, attr, classes)







ixnhttp = IxnHttp('10.200.22.48', 12345)
sessions = ixnhttp.sessions()
ixnhttp.current_session = sessions[0]

classes = {}
class_paths = [
    '/topology/deviceGroup/ethernet',
    '/topology/deviceGroup/ethernet/ipv4/pimV4Interface',
    '/topology/deviceGroup/ethernet/ipv4/igmpHost',
    '/topology/deviceGroup/ethernet/ipv4/bgpIpv4Peer',
    '/topology/deviceGroup/ethernet/ipv4/ospfv2',
    '/topology/deviceGroup/ethernet/ipv4/bfdv4Interface',
    '/topology/deviceGroup/ethernet/ipv6/mldHost',
    '/topology/deviceGroup/ethernet/ipv6/bgpIpv6Peer',
    '/topology/deviceGroup/ethernet/ipv6/ospfV3',
    '/topology/deviceGroup/ethernet/ipv6/bfdv6Interface',
    '/topology/deviceGroup/ethernet/mpls',
    '/topology/deviceGroup/ethernet/isisL3',
    '/topology/deviceGroup/ethernet/isisFabricPath',
    '/topology/deviceGroup/ethernet/dhcpv4client',
    '/topology/deviceGroup/ethernet/dhcpv6client',
    '/topology/deviceGroup/ethernet/pppoxclient',
    '/topology/deviceGroup/ethernet/pppoxserver',
    '/topology/deviceGroup/ethernet/ptp',
    '/topology/deviceGroup/ethernet/lacp',
    '/topology/deviceGroup/ethernet/staticLag',
]

config_mgmt = IxnConfigManagement(ixnhttp)
for class_path in class_paths:
    config_mgmt.new_config()
    href = ixnhttp.root.href
    for class_path_piece in class_path.split('/')[1:]:
        try:
            metadata = ixnhttp.help('%s/%s' % (href, class_path_piece))
            href = process_node(ixnhttp, href, metadata, classes)
        except Exception as e:
            print(e.message)

    query_result = IxnQuery(ixnhttp, href).node('.*', properties=['*']).go()
    process_query_result(ixnhttp, query_result, classes)


filename = '%s/../ixnetwork/IxnEmulationHosts.py' % os.path.dirname(os.path.realpath(__file__))
with open(filename, 'w') as fid:
    fid.write('from ixnetwork.IxnEmulationHost import IxnEmulationHost\n\n')
    keys = classes.keys()
    keys.sort()
    for key in keys:
        fid.write(classes[key])
    fid.flush()


