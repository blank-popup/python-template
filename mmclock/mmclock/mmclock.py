#-*- coding: utf-8 -*-
import threading
import _thread
import time
'''
Clock for timeout of execution, tictoc
'''

class TimeoutException(Exception):
    '''
    Custom exception to process timeout
    '''
    pass

def timeout(Seconds):
    '''
    Decoration for timeout
    Seconds: seconds to stop execution
    '''
    def wrapper_function(Function):
        def wrapper_arg(*args, **kwargs):
            def raise_keyboard_interrupt():
                _thread.interrupt_main()
            timer = threading.Timer(Seconds, raise_keyboard_interrupt, args=[])
            timer.start()
            try:
                rv = Function(*args, **kwargs)
            except KeyboardInterrupt as ki:
                rv = ki
            finally:
                if timer.is_alive():
                    timer.cancel()
            return rv
        return wrapper_arg
    return wrapper_function

# NAME_RETURN_VALUE = 'rv'
# NAME_EXCEPTION = 'except'

# def timeout(Seconds):
#     '''
#     Decoration for timeout
#     Seconds: seconds to stop execution
#     '''
#     def wrapper_function(Function):
#         def wrapper_arg(*args, **kwargs):
#             rv = {}
#             def raise_keyboard_interrupt():
#                 rv[NAME_EXCEPTION] = TimeoutException(f'Timeout exception {Function.__name__}')
#                 _thread.interrupt_main()
#             timer = threading.Timer(Seconds, raise_keyboard_interrupt, args=[])
#             timer.start()
#             try:
#                 rv[NAME_RETURN_VALUE] = Function(*args, **kwargs)
#             except KeyboardInterrupt as ki:
#                 if NAME_EXCEPTION not in rv:
#                     rv[NAME_EXCEPTION] = ki
#             except Exception as e:
#                 rv[NAME_EXCEPTION] = e
#             finally:
#                 if timer.is_alive():
#                     timer.cancel()
#             return rv
#         return wrapper_arg
#     return wrapper_function

class TicToc(object):
    '''
    Helper Class
    Use with 'with' like followings

    with TicToc('tictoc'):
        time.sleep(1.5)
    '''
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print(f'[{self.name}] ')
        print(f'Elapsed: {time.time() - self.tstart}')


def tictoc(Function):
    '''
    Decoration for tictoc
    Seconds: seconds to stop execution
    '''
    def wrapped(*args, **kwargs):
        start = time.time()
        rv = Function(*args, **kwargs)
        return (rv, time.time() - start)
    return wrapped
