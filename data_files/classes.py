import warnings
import functools
__author__ = 'Danyang'


def Override(interface_class):
    
    def overrider(method):
        try:
            assert (method.__name__ in dir(interface_class))
            return method
        except AssertionError:
            print method.__name__+" for "+interface_class.__name__

    return overrider


warnings.simplefilter('always', DeprecationWarning)


def Deprecated(func, msg=None):
    
    message = msg or "Use of deprecated function '{}`.".format(func.__name__)

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)

    return wrapper_func

