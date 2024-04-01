import time
from typing import Any, Callable


def measure_func(func: Callable[[], Any]) -> float:
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time