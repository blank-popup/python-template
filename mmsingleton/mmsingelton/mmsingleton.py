#-*- coding: utf-8 -*-
'''
Singleton class
'''

class MMSingleton(object):
    '''
    Base class of singleton
    '''
    instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls)
        return cls.instance
