#-*- coding: utf-8 -*-
import time

from mmclock import mmclock

def do_something(to):
    from time import sleep
    print('countdown started', flush=True)
    for ii in range(to, -1, -1):
        print(ii, end=', ', flush=True)
        sleep(1)
    print('countdown finished')

    return 18

@mmclock.timeout(2)
def quit_in_two_seconds():
    return do_something(5)

@mmclock.timeout(5)
def quit_in_five_seconds():
    return do_something(2)

@mmclock.tictoc
def tictoc_do_something():
    return do_something(3)

if __name__ == '__main__':

    rv = mmclock.timeout(2)(do_something)(5)
    if isinstance(rv, KeyboardInterrupt):
        print(f'Timeout during execution')
    else:
        print(f'{rv}')
    rv = mmclock.timeout(5)(do_something)(2)
    if isinstance(rv, KeyboardInterrupt):
        print(f'Timeout during execution')
    else:
        print(f'{rv}')

    rv = quit_in_two_seconds()
    if isinstance(rv, KeyboardInterrupt):
        print(f'Timeout during execution')
    else:
        print(f'{rv}')
    rv = quit_in_five_seconds()
    if isinstance(rv, KeyboardInterrupt):
        print(f'Timeout during execution')
    else:
        print(f'{rv}')

    print(f'============================')
    with mmclock.TicToc('tictoc'):
        time.sleep(2.5)

    print(f'============================')
    rv = mmclock.tictoc(do_something)(3)
    print(f'{rv}')

    rv = tictoc_do_something()
    print(f'{rv}')
