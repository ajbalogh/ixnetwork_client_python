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
        self._multivalue = IxnQuery(self._ixnhttp, self._multivalue_href) \
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
        """Get the current pattern of the multivalue
        
        :returns: str: singleValue|counter|alternate|random|repeatableRandom|valueList|string|custom
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.pattern.value
    
    @property
    def single_value(self):
        """Get the single value

        :returns: str or None: A valid singlevalue or None if the pattern is not singleValue
        """
        if self._multivalue.pattern.value == 'singleValue':
            return self._multivalue.singleValue.value.value
        return None

    @single_value.setter
    def single_value(self, value):
        """Changes the pattern to singleValue and sets the value"""
        self._multivalue.create_singleValue(payload={'value': value})
        self._refresh()

    def get_counter(self):
        """Get the counter variables

        :returns: counter object or None: A valid counter object or None if the pattern is not counter
        """
        if self._multivalue.pattern.value == 'counter':
            return self._multivalue.counter
        return None

    def set_counter(self, start=None, step=None, direction=None):
        """Changes the pattern to counter and sets the values"""
        if self.pattern is not 'counter':
            self._multivalue.create_counter()
            self._refresh()
        if start is not None:
            self._multivalue.counter.start.value = start
        if step is not None:
            self._multivalue.counter.start.value = step
        if direction is not None:
            self._multivalue.counter.direction.value = direction
        self._multivalue.counter.update()
        self._refresh()
