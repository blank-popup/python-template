#-*- coding: utf-8 -*-
import logging
import logging.handlers

from mmlogit import mmlogit
import otherfile


# Define logger using current module
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Add handlers(consol, file) to root logger
    if len(logging.getLogger().handlers) < 1:
        mmlogit.set_root_logger(f'test_logit.log')

    # Use logger like followings
    logger.critical(f'main critical')
    logger.error(f'main error')
    logger.warning(f'main warning')
    logger.info(f'main info')
    logger.debug(f'main debug')

    # Test logging at other module
    otherfile.test_sub_function()
