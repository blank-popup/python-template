#-*- coding: utf-8 -*-
import logging
import logging.handlers
import sys
'''
General logging configuration
'''


logger = logging.getLogger(__name__)
# To log traceback
sys.excepthook = lambda excType, excValue, traceback: handle_excepthook(logger, excType, excValue, traceback)

def set_root_logger(filepath=None, level=logging.DEBUG):
    '''
    Set root logger
    Add consol and file handler
    Consol handler is StreamHandler
    File handler is RotatingFileHandler
        Max file size: 1024*1024*1024
        The count of backup file: 10
        Encoding: utf-8
    '''
    root = logging.getLogger()
    root.setLevel(level)
    formatter = logging.Formatter(u'[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s (%(pathname)s, %(lineno)s)')
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    root.addHandler(streamHandler)
    # If filepath is not None, Use file handler
    if filepath is not None:
        fileHandler = logging.handlers.RotatingFileHandler(
            filepath, mode='a',
            maxBytes=1024*1024*1024,
            backupCount=10,
            encoding='utf-8'
        )
        fileHandler.setFormatter(formatter)
        root.addHandler(fileHandler)

    # # Test logging
    # logger.critical(f'logger py logging test critial')
    # logger.error(f'logger py logging test error')
    # logger.warning(f'logger py logging test warning')
    # logger.info(f'logger py logging test info')
    # logger.debug(f'logger py logging test debug')

def handle_excepthook(logger, excType, excValue, traceback):
    '''Exception handler for sys.excepthook'''
    logger.error(f'Logging an uncaught exception', exc_info=(excType, excValue, traceback))

def test_exception_traceback():
    '''Method for test logging traceback'''
    exception = 1 / 0
    return exception
