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
                .go()

    @property
    def pattern(self):
        self._refresh()
        return self._multivalue.attributes.pattern.value
    
    def getSingleValue(self):
        if self._singleValue is None:
            self._singleValue = self._ixnhttp.get('%s/singleValue' % self._multivalue_href)    
            
    def setSingleValue(self, value):
        """Changes the pattern to singleValue and sets the value"""
        self._singleValue = value

    def update(self):
        payload = {
            'value': self._singleValue
        }
        self._ixnhttp.post('%s/singleValue' % self._multivalue_href, payload)