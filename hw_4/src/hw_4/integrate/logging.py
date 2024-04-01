
import logging
import os
import sys


def get_logger(name: str)-> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s,%(msecs)03d - %(message)s', datefmt='%H:%M:%S')
    handler = logging.FileHandler("integrate_log.txt")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger