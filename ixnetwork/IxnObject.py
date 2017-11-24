"""Dynamically add attributes, operations based on meta data
"""
from ixnetwork.IxnDynAttr import IxnDynAttr


class IxnObject(object):

    def __init__(self, ixnhttp, query_result):
        self._ixnhttp = ixnhttp
        from ixnetwork.IxnQuery import IxnQuery
        setattr(self, 'id', query_result.id if hasattr(query_result, 'id') else None)
        setattr(self, 'href', query_result.href)
        setattr(self, 'attributes', lambda: None)
        setattr(self, 'operations', lambda: None)
        setattr(self, 'query', IxnQuery(self._ixnhttp, query_result.href))
        self._meta_data = self._ixnhttp._get_meta_data(query_result.href)
        self._add_attributes(query_result)
        self._add_operations(query_result)
        self._process_child_instances(query_result)

    def _get_dyn_attrs(self):
        dyn_attrs = []
        for attribute in self._meta_data.attributes:
            if hasattr(self.attributes, attribute.name):
                dyn_attr = getattr(self.attributes, attribute.name)
                dyn_attrs.append(dyn_attr)
        return dyn_attrs

    def _add_attributes(self, result):
        for attribute in self._meta_data.attributes:
            if hasattr(result, attribute.name):
                value = getattr(result, attribute.name)
                setattr(self.attributes, attribute.name, IxnDynAttr(self._ixnhttp, attribute, value))

    def _add_operations(self, result):
        def dump_operation():
            print( 'href: %s' % (self.href))
            for dyn_attr in self._get_dyn_attrs():
                print("%s: %s" % (dyn_attr.name, dyn_attr.value))
        setattr(self, 'dump', dump_operation)

        if self._meta_data.remove is True:
            def delete_operation():
                self._ixnhttp.delete(self.href)
            delete_operation.__doc__ = 'Delete this %s object' % (self._meta_data.name)
            setattr(self, 'delete', delete_operation)
        
        update = False
        for attribute in self._meta_data.attributes:
            if attribute.readOnly is False:
                update = True
                break
        if update is True:
            def update_operation():
                updates = {}
                for dyn_attr in self._get_dyn_attrs():
                    if dyn_attr.is_dirty is True and dyn_attr.is_multivalue is False:
                        updates[dyn_attr.name] = dyn_attr.value
                if len(updates.keys()) > 0:
                    self._ixnhttp.patch(self.href, updates)
                    self.refresh()
            update_operation.__doc__ = 'Update this %s object excluding multivalues which are handled immediately by the IxnMultivalue class' % (self._meta_data.name)
            setattr(self, 'update', update_operation)
            
        if len(self._get_dyn_attrs()) > 0:
            def refresh_operation():
                refreshed_attributes = self._ixnhttp._send_recv('GET', self.href)
                for dyn_attr in self._get_dyn_attrs():
                    value = getattr(refreshed_attributes, dyn_attr.name)
                    setattr(self.attributes, dyn_attr.name, IxnDynAttr(self._ixnhttp, dyn_attr._meta_data, value))
            refresh_operation.__doc__ = 'Refresh the attributes of this %s object' % (self._meta_data.name)
            setattr(self, 'refresh', refresh_operation)
        
        for operation in self._meta_data.operations:
            operation_name = operation.operation.lower()
            def method_operation(payload=None, operation_name=operation_name):
                if self.href[-1] == '/':
                    url = '%soperations/%s' %(self.href, operation_name)
                else:
                    url = '%s/operations/%s' %(self.href, operation_name)
                return self._ixnhttp.post(url, payload)
            setattr(self.operations, operation_name, method_operation)
            getattr(self.operations, operation_name).__doc__ = operation.description

        if len(self._meta_data.children) > 0:
            def _create_child(child_name, count=1, payload=None):
                if payload is None:
                    payload = []
                    for i in range(0, count):
                        payload.append({})
                full_url = '%s/%s' % (self.href, child_name)
                full_url = full_url.replace('//', '/')
                response = self._ixnhttp.post(full_url, payload)
                new_objects = []
                for link in response.links:
                    new_object = self._ixnhttp.get(link.href)
                    setattr(new_object, 'href', link.href)
                    new_objects.append(IxnObject(self._ixnhttp, new_object))
                if len(new_objects) == 1:
                    return new_objects[0]
                else:
                    return new_objects
            _create_child.__doc__ = 'Create a child object under this %s object' % (self._meta_data.name)
            setattr(self, 'create_child', _create_child)
    
    def _process_child_instances(self, result):
        for child in self._meta_data.children:
            if hasattr(result, child.name):
                value = getattr(result, child.name)
                if isinstance(value, list):
                    ixnobjects = []
                    for item in value:
                        ixnobjects.append(IxnObject(self._ixnhttp, item))
                else:
                    ixnobjects = IxnObject(self._ixnhttp, value)
                setattr(self, child.name, ixnobjects)

    