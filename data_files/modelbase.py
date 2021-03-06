import six

__author__ = 'Daniel'



class NaiveModelField(object):
    
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class ModelField(object):
    
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class ModelBaseMeta(type):
    def __new__(mcs, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, ModelField):
                value.name = key
                value.internal_name = '_' + key

        cls = type.__new__(mcs, name, bases, class_dict)
        return cls


class Model(six.with_metaclass(ModelBaseMeta)):
    pass