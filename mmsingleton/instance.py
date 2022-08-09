#-*- coding: utf-8 -*-
import mmsingelton.mmsingleton


class UniqueClass(mmsingelton.mmsingleton.Singleton):
    def __init__(self, *args, **kwargs):
        super(UniqueClass, self).__init__()

if __name__ == '__main__':
    unique0 = UniqueClass()
    unique1 = UniqueClass()

    print(f'ID of unique0: {id(unique0)}')
    print(f'ID of unique1: {id(unique1)}')
