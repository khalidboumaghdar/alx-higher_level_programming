#!/usr/bin/python3
'''Module for lookup methode.'''



def lookup(obj):
    '''looks up object attributes and methodods.
    Args:
        obj(object) : the object to list.

    returns:
            list : the list of attributes.
    '''
    return dir(obj)
