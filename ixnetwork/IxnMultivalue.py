from ixnetwork.IxnQuery import IxnQuery
"""
Encapsulates a multivalue
"""

class IxnMultivalue(object):
    """An internal class that exposes a SDM multivalue using SDM meta data. """
    
    def __init__(self, ixnhttp, multivalue_href):
        self._ixnhttp = ixnhttp
        self._multivalue_href = multivalue_href
        self._multivalue = None

    def _refresh(self):
        if self._multivalue is None:
            self._multivalue = IxnQuery(ixnhttp, self._multivalue_href) \
                .node('multivalue', properties=['availablePatterns', 'count', 'format', 'pattern']) \
                .node('singleValue', properties=['*']) \
                .node('counter', properties=['*']) \
                .node('alternate', properties=['*']) \
                .node('random', properties=['*']) \
                .node('repeatableRandom', properties=['*']) \
                .node('valueList', properties=['*']) \
                .node('string', properties=['*']) \
                .node('custom', properties=['*']) \
                .node('nest', properties=['*']) \
                .go()

    @property
    def pattern(self):
        self._refresh()
        return self._multivalue.attributes.pattern.value
    
    def getSingleValue(self):
        if self._multivalue.pattern.value == 'singleValue':
            return self._multivalue.singleValue.value.value
            
    def setSingleValue(self, value):
        """Changes the pattern to singleValue and sets the value"""
        self._ixnhttp._multivalue.create_singleValue({'value': value})
        self._refresh()
