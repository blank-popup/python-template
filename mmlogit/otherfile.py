#-*- coding: utf-8 -*-
import logging


# Define logger using current module
logger = logging.getLogger(__name__)

def test_sub_function():
    # Logging message is propagated to root logger and root logger handles the message
    logger.critical(f'sub critical')
    logger.error(f'sub error')
    logger.warning(f'sub warning')
    logger.info(f'sub info')
    logger.debug(f'sub debug')
