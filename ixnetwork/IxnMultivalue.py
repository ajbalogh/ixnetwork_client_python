"""
Encapsulates a multivalue
"""

class IxnMultivalue(object):
    """An internal class that exposes a SDM multivalue using SDM meta data. 
    """
    SINGLE_VALUE = 'singleValue'
    COUNTER = 'counter'
    ALTERNATE = 'alternate'
    RANDOM = 'random'
    REPEATABLE_RANDOM = 'repeatableRandom'
    VALUE_LIST = 'valueList'
    STRING = 'string'
    CUSTOM = 'custom'
    NEST = 'nest'

    def __init__(self, ixnhttp, multivalue_href):
        self._ixnhttp = ixnhttp
        self._multivalue_href = multivalue_href
        self._multivalue = None

    def _refresh(self):
        from ixnetwork.IxnQuery import IxnQuery
        self._multivalue = IxnQuery(self._ixnhttp, self._multivalue_href) \
            .node('multivalue', properties=['availablePatterns', 'count', 'format', 'pattern', 'source']) \
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
    def href(self):
        """Get the href of the multivalue
        
        :returns: str: 
        """
        return self._multivalue_href

    @property
    def pattern(self):
        """Get the current pattern of the multivalue
        
        :returns: str: singleValue|counter|alternate|random|repeatableRandom|valueList|string|custom
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.pattern.value

    @property
    def available_patterns(self):
        """Get all available patterns for the multivalue
        
        :returns: list[str]: a list of one or more of singleValue|counter|alternate|random|repeatableRandom|valueList|string|custom
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.availablePatterns.value
    
    @property
    def format(self):
        """Get the format of values that can be get/set in this object
        
        :returns: str: the format of the value
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.format.value

    @property
    def count(self):
        """Get the total number of values represented by this multivalue
        
        :returns: number: the count of values
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.count.value

    @property
    def source(self):
        """Get the source node/attribute of this multivalue
        
        :returns: str: source node/attribute
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.source.value

    def get_values(self, start_index=0, count=None):
        """Get values represented by this multivalue
        
        :returns: list[str]: a list of values represented by this multivalue
        """
        if self._multivalue is None:
            self._refresh()
        if count is None:
            count = self.count
        if count > self.count:
            count = self.count
        values = self._multivalue.operations.getvalues({'arg1': self._multivalue_href, 'arg2': start_index, 'arg3': count})
        return values.result

    def dump(self):
        """Print a summary of this multivalue object"""
        if self._multivalue is None:
            self._refresh()
        print('source:\t%s' % self.source)
        print('\tpatt:\t%s  available:%s' % (self.pattern, "|".join(self.available_patterns)))
        print('\tcount:\t%s' % self.count)
        print('\tformat:\t%s' % self.format)
        print('\tvalues:\t%s...' % ' '.join(self.get_values(0, 3)))

    @property
    def single_value(self):
        """Get the single value

        :returns: str or None: A valid singlevalue or None if the pattern is not singleValue
        """
        if self._multivalue.attributes.pattern.value == IxnMultivalue.SINGLE_VALUE:
            return self._multivalue.singleValue.attributes.value.value
        return None

    @single_value.setter
    def single_value(self, value):
        """Changes the pattern to singleValue and sets the value"""
        if self._multivalue is None:
            self._refresh()
        if self.pattern == IxnMultivalue.SINGLE_VALUE:
            self._multivalue.singleValue.attributes.value.value = value
            self._multivalue.singleValue.update()
        else:
            self._multivalue.create_singleValue(payload={'value': value})
            self._refresh()

    @property
    def alternate(self):
        """Get the alternate value

        :returns: str or None: A valid alternate value or None if the pattern is not alatenate
        """
        if self._multivalue.attributes.pattern.value == IxnMultivalue.ALTERNATE:
            return self._multivalue.alternate.attributes.value.value
        return None

    @single_value.setter
    def alternate(self, value):
        """Changes the pattern to alternate and sets the value"""
        if self._multivalue is None:
            self._refresh()
        if self.pattern == IxnMultivalue.ALTERNATE:
            self._multivalue.alternate.attributes.value.value = value
            self._multivalue.alternate.update()
        else:
            self._multivalue.create_alternate(payload={'value': value})
            self._refresh()

    def get_counter(self):
        """Get the counter variables

        :returns: counter object or None: A valid counter object or None if the pattern is not counter
        """
        if self._multivalue.pattern.value == IxnMultivalue.COUNTER:
            return self._multivalue.counter
        return None

    def set_counter(self, start=None, step=None, direction=None):
        """Changes the pattern to counter and sets the values"""
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.COUNTER:
            self._multivalue.create_counter()
            self._refresh()
        if start is not None:
            self._multivalue.counter.attributes.start.value = start
        if step is not None:
            self._multivalue.counter.attribues.start.value = step
        if direction is not None:
            self._multivalue.counter.attributes.direction.value = direction
        self._multivalue.counter.update()
        self._refresh()

    def _refresh_check(self, expected_pattern):
        if self._multivalue is None:
            self._refresh()
        if self.pattern is not 'counter':
            self._multivalue.create_counter()
            self._refresh()

    @property
    def value_list(self):
        """Get the value list

        :returns: str or None: A valid singlevalue or None if the pattern is not singleValue
        """
        if self._multivalue.attributes.pattern.value == IxnMultivalue.VALUE_LIST:
            return self._multivalue.valueList.attributes.values.value
        return None

    @value_list.setter
    def value_list(self, values):
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.VALUE_LIST:
            self._multivalue.create_valueList()
            self._refresh()
        self._multivalue.valueList.attributes.values.value = values
        self._multivalue.valueList.update()

    def set_random(self):
        """Set the multivalue pattern to random."""
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.RANDOM:
            self._multivalue.create_random()
            self._refresh()

    def set_repeatable_random(self, count=None, fixed=None, mask=None, seed=None):
        """Changes the pattern to counter and sets the values"""
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.REPEATABLE_RANDOM:
            self._multivalue.create_repeatableRandom()
            self._refresh()
        if count is not None:
            self._multivalue.repeatableRandom.attributes.count.value = count
        if fixed is not None:
            self._multivalue.repeatableRandom.attribues.fixed.value = fixed
        if mask is not None:
            self._multivalue.repeatableRandom.attributes.mask.value = mask
        if seed is not None:
            self._multivalue.repeatableRandom.attributes.seed.value = seed
        self._multivalue.repeatableRandom.update()
        self._refresh()

    def get_repeatable_random(self):
        """Get the repeatableRandom variables

        :returns: repeatableRandom object or None: A valid repetableRandom object or None if the pattern is not repetableRandom
        """
        if self._multivalue.pattern.value == IxnMultivalue.REPEATABLE_RANDOM:
            return self._multivalue.repeatableRandom
        return None
