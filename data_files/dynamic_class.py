__author__ = 'Daniel'


class LazyDataStore(object):
    
    def __init__(self):
        self.existing_attr = 5

    def __getattr__(self, name):
        
        value = 'Value for % s' % name
        setattr(self, name, value)
        return value


class LazyDataStore2(object):
    def __init__(self):
        self.existing_attr = 5

    def __getattribute__(self, name):
        
        try:
            return super(LazyDataStore2, self).__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

    def __setattr__(self, name, value):
        
        print "Aspect: Save some data to the DB log"
        super(LazyDataStore2, self).__setattr__(name, value)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        
        _data = super(DictionaryDB, self).__getattribute__('_data')
        return _data[name]
