"""
IxnQuery Overview
--------------------------------
The low level class IxnQuery allows access to the entire low level IxNetwork hierarchy.
It allows access to objects if the json feature is not yet available.
It dynamically builds objects based on the return of the query and the type of object.
Each object has .attributes, .operations and an update/delete method depending on the type of object.
Attributes are returned by specifying them in the properties list of the node.
The properties list supports regex so if you want all attributes returned specify properties=['*'].
"""
from ixnetwork.IxnObject import IxnObject


class IxnQuery(object):
    """An internal class that exposes the query API. """

    def __init__(self, ixnhttp, starting_url):
        self._ixnhttp = ixnhttp
        self._starting_url = starting_url
        self.clear()

    def clear(self):
        self._select = {
            'from': self._starting_url,
            'nodes': [],
            'inlines': []
        }
        self._query = {
            'selects': []
        }
        self._query['selects'].append(self._select)
        return self

    def node(self, node_name, properties=[], where=[]):
        """Add a node to include in the search of the hierarchy
        
        Args: 
            node_name: the name of the node
            properties: a list of the property names to include in the response
            where: a list of where filters, each filter should be of the format:
                {
                    'property': 'the name of the property', 
                    'regex': 'a regex filter for that property'
                }

        Returns: 
            An object
            OR
            List of objects
            OR
            None if there are no matches        
        """
        self._select['nodes'].append(
            {
                'node': node_name,
                'properties': properties,
                'where': where
            }
        )
        return self

    def inline(self, *args):
        self._select['inlines'] = []
        for arg in args:
            if arg == IxnHttp.Multivalue:
                self._select['inlines'].append(
                    {
                        "node": "multivalue",
                        "properties": ["source", "pattern", "values"]
                    }
                )
                self._select['inlines'].append(
                    {
                        "node": "^(?:singleValue|alternate|distributed|counter|random|repeatableRandom|custom|customDistributed|string]",
                        "properties": ["*"]
                    }
                )
            elif arg == IxnHttp.Vport:
                self._select['inlines'].append(
                    {
                        "node": "vport",
                        "properties": ["*"]
                    }
                )
        return self

    def go(self):
        """Starts the search using the query parameters provided to the search object

        Args: 
            None

        Returns: 
            An object with all nested matches as objects
            None If the query has no matches
        """
        async_response = self._ixnhttp.post('/operations/query', self._query)
        if async_response.state == 'SUCCESS':
            if isinstance(async_response.result[0], list):
                ixnobjects = []
                for item in async_response.result[0]:
                    ixnobjects.append(IxnObject(self._ixnhttp, item))
                return ixnobjects
            else:
                return IxnObject(self._ixnhttp, async_response.result[0])
        else:
            return None

