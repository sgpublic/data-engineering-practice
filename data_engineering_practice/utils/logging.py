import logging
from logging import Logger

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def new_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    return logger
