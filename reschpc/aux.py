#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'

import sys

def byte2dict(x):
    """
    Converts a byte object into a dictionary
    Returns a dictionary object 
    """
    try:
        s = x.decode("utf-8")
        s = s.replace(":true", ":True")
        s = s.replace(":false", ":False")
        s = s.replace(":null", ":None")
        d = eval(s)
    except Exception as err:
        print(f"  ERROR  aux::byte2dict -> {err}")
        sys.exit()
    return d
