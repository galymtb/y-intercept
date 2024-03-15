import logging
import sys


def get_logger(filename: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt="[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    handler_1 = logging.FileHandler(filename, 'a', 'utf-8')
    handler_1.setFormatter(formatter)

    handler_2 = logging.StreamHandler(sys.stdout)
    handler_2.setFormatter(formatter)

    logger.addHandler(handler_1)
    logger.addHandler(handler_2)

    return logger