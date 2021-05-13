__author__ = 'Daniel'


def _add_tests(generator):
    
    def class_decorator(cls):
        
        for f, args in generator():
            
            test = lambda self, args=args, f=f: f(self, *args)

            test.__name__ = "test_%s_%s" % (f.__name__, args[0])
            setattr(cls, test.__name__, test)
        return cls

    return class_decorator