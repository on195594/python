#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import types

def log(arg):
    if isinstance(arg, types.FunctionType):
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print('begin call')
            arg(*args, **kw)
            print('end call')
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(arg, 'begin call')
                func(*args, **kw)
                print('end call')
            return wrapper
        return decorator

@log
def f1():
    print('This is f1.')

@log('Lxy')
def f2():
    print('This is f2.')

f1()
f2()
