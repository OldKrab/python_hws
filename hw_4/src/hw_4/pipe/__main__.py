import codecs
import logging
import multiprocessing
from multiprocessing.connection import Connection
import sys
import time


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%H:%M:%S")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)


def a_func(input: Connection, output: Connection):
    while True:
        if input.poll():
            data: str = input.recv()
            res = data.lower()
            output.send(res)
        time.sleep(5)


def b_func(input: Connection, output: Connection):
    while True:
        data = input.recv()
        res = codecs.encode(data, "rot_13")
        logger.info(f"B output: {res}")
        output.send(res)


(main_output, a_input) = multiprocessing.Pipe()
(a_output, b_input) = multiprocessing.Pipe()
(b_output, main_input) = multiprocessing.Pipe()

a_process = multiprocessing.Process(target=a_func, args=(a_input, a_output))
b_process = multiprocessing.Process(target=b_func, args=(b_input, b_output))
a_process.start()
b_process.start()
while True:
    data = input()
    if data == "":
        break
    logger.info(f"User input: {data}")
    main_output.send(data)

a_process.terminate()
b_process.terminate()