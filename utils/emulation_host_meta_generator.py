import StringIO
import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, '%s/..' % os.path.dirname(os.path.abspath(__file__)))
from ixnetwork.IxnHttp import IxnHttp


def process_node(metadata, class_name):
    # build find
    expected_states = []
    attr_doc_string = '%s"""Find specific %s emulated host sessions using a virtual port name or a parent emulation host and optional filters.\n' % (' ' * 8, metadata.custom.name)
    attr_doc_string += '%sFilter values can be a single value or a list of values, see the specific **filter information below.\n\n' % (' ' * 12)
    attr_doc_string += '%svport_name: string (The topology that contains the vport with this name will be used as the starting point of the search)\n' % (' ' * 12)
    attr_doc_string += '%semulation_host: IxnEmulationHost (A parent emulation host that will be used as the starting point of the search)\n' % (' ' * 12)
    attr_doc_string += '%s**filters:\n' % (' ' * 12)
    for attribute in metadata.custom.attributes:
        if attribute.deprecated is False:
            if attribute.type.name == 'object':
                continue
            if attribute.type.name == 'list' and attribute.type.innerType.name == 'enum':
                expected_states = attribute.type.innerType.enums
                continue
            attr_doc_string += '%s%s: %s' % (' ' * 16, attribute.name, attribute.type.name)
            attr_doc_string += '\n'
    attr_doc_string += '%s"""\n' % (' ' * 8)

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
    if len(expected_states) > 0:
        for operation in metadata.custom.operations:
            if len(operation.args) == 2 and operation.args[1].type.name == 'string':
                fid.write('%sdef %s(self, expected_state=None, timeout=None):\n' % (' ' * 4, operation.operation.lower()))
                fid.write('%s"""%s\n' % (' ' * 8, ' '.join(operation.description.split())))
                fid.write('%sFor expected_state options see the class state variables\n' % (' ' * 12))
                fid.write('%s"""\n' % (' ' * 8))
                fid.write('%ssuper(%s, self).call_operation(\'%s\', expected_state, timeout)\n' % (' ' * 8, class_name, operation.operation))
                fid.write('\n')
    fid.write('\n')

    classes[metadata.custom.name] = fid.getvalue()
    fid.close()
    print('GENERATED: %s' % class_name)

def process_class(path, name):
    if name in classes.keys():
        return
    if name in ['connector', 'item', 'port', 'tlvProfile', 'learnedInfo', 'genericProtocol','packetInList']:
        return
    try:
        metadata = ixnhttp.help(path)
        class_name = 'Ixn%s%sEmulation' % (metadata.custom.name[0].upper(), metadata.custom.name[1:])
        process_node(metadata, class_name)
        for child in metadata.custom.children:
            process_class(child.path, child.name)
    except:
        print('skipping %s' % name)

ixnhttp = IxnHttp('10.200.22.48', 12345)
sessions = ixnhttp.sessions()
ixnhttp.current_session = sessions[0]


classes = {}
process_class('/topology', 'topology')

filename = '%s/../ixnetwork/IxnEmulationHosts.py' % os.path.dirname(os.path.realpath(__file__))
with open(filename, 'w') as fid:
    fid.write('from ixnetwork.IxnEmulationHost import IxnEmulationHost\n\n')
    keys = classes.keys()
    keys.sort()
    for key in keys:
        fid.write(classes[key])
    fid.flush()


