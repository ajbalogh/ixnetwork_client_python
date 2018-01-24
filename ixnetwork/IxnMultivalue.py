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
    REPEATABLE_RANDOM_RANGE = 'repeatableRandomRange'
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
            .node('repeatableRandomRange', properties=['*']) \
            .node('valueList', properties=['*']) \
            .node('string', properties=['*']) \
            .node('custom', properties=['*']) \
            .node('nest', properties=['*']) \
            .node('increment', properties=['*']) \
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
        
        :returns: str: singleValue|counter|alternate|random|repeatableRandom|repeatableRandomRange|valueList|string|custom
        """
        if self._multivalue is None:
            self._refresh()
        return self._multivalue.attributes.pattern.value

    @property
    def available_patterns(self):
        """Get all available patterns for the multivalue
        
        :returns: list[str]: a list of one or more of singleValue|counter|alternate|random|repeatableRandom|repeatableRandomRange|valueList|string|custom
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
        
        start_index: 0 based offset in the list of values
        count: default is all values

        :returns: list[str]: a list of string values represented by this multivalue
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
            self._multivalue.create_child('singleValue', payload={'value': value})
            self._refresh()

    @property
    def alternate(self):
        """Get the alternate value

        :returns: str or None: A valid alternate value or None if the pattern is not alatenate
        """
        if self._multivalue.attributes.pattern.value == IxnMultivalue.ALTERNATE:
            return self._multivalue.alternate.attributes.value.value
        return None

    @alternate.setter
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
            self._multivalue.create_child('counter')
            self._refresh()
        if start is not None:
            self._multivalue.counter.attributes.start.value = start
        if step is not None:
            self._multivalue.counter.attributes.step.value = step
        if direction is not None:
            self._multivalue.counter.attributes.direction.value = direction
        self._multivalue.counter.update()
        self._refresh()

    def _refresh_check(self, expected_pattern):
        if self._multivalue is None:
            self._refresh()
        if self.pattern is not 'counter':
            self._multivalue.create_child('counter')
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
            self._multivalue.create_child('valueList')
            self._refresh()
        self._multivalue.valueList.attributes.values.value = values
        self._multivalue.valueList.update()

    def set_custom(self, start_value=None, step_value=None):
        """ Change the pattern to Custom using only start and step """
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.CUSTOM:
            payload = {}
            if start_value is not None:
                payload['start'] = start_value
            if step_value is not None:
                payload['step'] = step_value
            custom_object = self._multivalue.create_child(IxnMultivalue.CUSTOM, payload=payload)
        else:
            if start_value is not None:
                self._multivalue.custom.start.value = start_value
            if step_value is not None:
                self._multivalue.custom.step.value = step_value
            custom_object =self._multivalue.custom.update()

        self._multivalue_href = custom_object.href
        self._refresh()
        return self

    @property
    def get_increment(self):
        return self._multivalue.increment

    def set_custom_increment(self, value = None, count = None, href=None):
        """
        This will work on top of custom or increment node
        It will modify value and count when call with href
        """
        self._refresh()

        if href is None:
            if len(self.get_increment) >= 1:
                self._multivalue_href = self.get_increment[0].href
                self._refresh()
                if value is not None:
                    self._multivalue.attributes.value.value = value
                if count is not  None:
                    self._multivalue.attributes.count.value = count
                self._multivalue.update()
            else:
                payload = {}
                if value is not None:
                    payload['value'] = value
                if count is not None:
                    payload['count'] = count
                increment_object = self._multivalue.create_child('increment', payload=payload)
                self._multivalue_href = increment_object.href
        else:
            self._multivalue_href = href
            self._refresh()
            if value is not None:
                self._multivalue.attributes.value.value = value
            if count is not  None:
                self._multivalue.attributes.count.value = count
            self._multivalue.update()
        self._refresh()
        return self

    def set_custom_basic(self, start_value, step_value, repeat_each_value, sequence_length):
        """ This is a high level utility function to create custom basic pattern"""
        # set default value to 1 if value <0
        repeat_each_value = repeat_each_value if repeat_each_value <=0 else 1
        sequence_length = sequence_length if sequence_length <=0 else 1
        null_value = self.set_custom(start_value = start_value)._multivalue.attributes.step.value
        self.set_custom_increment(step_value, sequence_length).set_custom_increment(null_value, repeat_each_value)

    def set_random(self):
        """Set the multivalue pattern to random."""
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.RANDOM:
            self._multivalue.create_child('random')
            self._refresh()

    def set_repeatable_random(self, count=None, fixed=None, mask=None, seed=None):
        """Changes the pattern to repetableRandom and sets the values"""
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.REPEATABLE_RANDOM:
            payload = {}
            if count is not None:
                payload['count'] = count
            if fixed is not None:
                payload['fixed'] = fixed
            if mask is not None:
                payload['mask'] = mask
            if seed is not None:
                payload['seed'] = seed
            self._multivalue.create_child(IxnMultivalue.REPEATABLE_RANDOM, payload=payload)
            self._refresh()
        else:
            if count is not None:
                self._multivalue.repeatableRandom.attributes.count.value = count
            if fixed is not None:
                self._multivalue.repeatableRandom.attributes.fixed.value = fixed
            if mask is not None:
                self._multivalue.repeatableRandom.attributes.mask.value = mask
            if seed is not None:
                self._multivalue.repeatableRandom.attributes.seed.value = seed
            self._multivalue.repeatableRandom.update()
            self._refresh()

    def get_repeatable_random(self):
        """Get the repeatableRandom variables

        :returns: A valid repeatableRandom object or None if the pattern is not repeatableRandom
        """
        if self._multivalue.pattern.value == IxnMultivalue.REPEATABLE_RANDOM:
            return self._multivalue.repeatableRandom
        return None

    def set_repeatable_random_range(self, min=None, max=None, step=None, seed=None):
        """Changes the pattern to repeatableRandomRange and sets the values"""
        if self._multivalue is None:
            self._refresh()
        if self.pattern != IxnMultivalue.REPEATABLE_RANDOM_RANGE:
            payload = {}
            if min is not None:
                payload['min'] = min
            if max is not None:
                payload['max'] = max
            if step is not None:
                payload['step'] = step
            if seed is not None:
                payload['seed'] = seed
            self._multivalue.create_child(IxnMultivalue.REPEATABLE_RANDOM_RANGE, payload=payload)
            self._refresh()
        else:
            if min is not None:
                self._multivalue.repeatableRandomRange.attributes.min.value = min
            if max is not None:
                self._multivalue.repeatableRandomRange.attributes.max.value = max
            if step is not None:
                self._multivalue.repeatableRandomRange.attributes.step.value = step
            if seed is not None:
                self._multivalue.repeatableRandomRange.attributes.seed.value = seed
            self._multivalue.repeatableRandomRange.update()
            self._refresh()

    def get_repeatable_random_range(self):
        """Get the repeatableRandomRange variables

        :returns: A valid repeatableRandomRange object or None if the pattern is not repeatableRandomRange
        """
        if self._multivalue.pattern.value == IxnMultivalue.REPEATABLE_RANDOM_RANGE:
            return self._multivalue.repeatableRandomRange
        return None
