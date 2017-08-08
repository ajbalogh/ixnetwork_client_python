"""Encapsulates an attribute

also includes IxnMultivalue
"""
from ixnetwork.IxnMultivalue import IxnMultivalue


class IxnDynAttr(object):
    """An internal class that exposes SDM attributes using SDM meta data. """
    
    def __init__(self, ixnhttp, meta_data, value):
        self._meta_data = meta_data
        self._dirty = False
        if self._meta_data.type.name == 'href' and any('multivalue' in href for href in self._meta_data.type.hrefs):
            self._value = IxnMultivalue(ixnhttp, value)
            def session_id_operation(match, port_count=None, port_offset=None):
                multivalue = ixnhttp.get('%s?includes=count,values' % self._value.href)
                session_ids = []
                start_index = int(0)
                end_index = int(multivalue.count)
                if port_count is not None and port_offset is not None:
                    port_range = multivalue.count / port_count
                    start_index = int((port_offset - 1) * port_range)
                    end_index = int(start_index + port_range)
                session_id = int(start_index + 1)
                for value in multivalue.values[start_index:end_index]:
                    if value in match:
                        session_ids.append(session_id)
                    session_id += 1
                return session_ids
            setattr(self, 'get_session_ids', session_id_operation)
        else:
            self._value = value

    @property
    def name(self):
        return self._meta_data.name

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if self._meta_data.readOnly is True or isinstance(self._value, IxnMultivalue):
            raise Exception('%s is read only and cannot be set' % (self._meta_data.name))
        if self._value != value:
            self._value = value
            self._dirty = True

    @property
    def is_dirty(self):
        return self._dirty   

    @property
    def is_read_only(self):
        return self._meta_data.readOnly

    @property
    def is_multivalue(self):
        return isinstance(self._value, IxnMultivalue)

    @property
    def type_info(self):
        name = self._meta_data.type.name
        if name == 'enum':
            return 'string (%s)' % ', '.join(self._meta_data.type.enums)
        elif name == 'href':
            return 'string (%s)' % ', '.join(self._meta_data.type.hrefs)
        else:
            return name

    @property
    def description(self):
        return self._meta_data.description


