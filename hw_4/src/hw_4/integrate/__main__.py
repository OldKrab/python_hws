import math
from typing import Callable
from concurrent.futures import (
    Executor,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
)
import multiprocessing
from hw_4.integrate.logging import get_logger
from hw_4.measure import measure_func

logger = get_logger(__name__)


def integrate_chunk(f: Callable[[float], float], chunk: tuple[int, int], a: float, step: float) -> float:
    start, end = chunk
    logger.info(f"Integrating iters in range [{start}, {end})...")
    acc_chunk = 0
    for i in range(start, end):
        acc_chunk += f(a + i * step) * step
    return acc_chunk


def integrate(
    f: Callable[[float], float],
    a: float,
    b: float,
    *,
    n_jobs=1,
    n_iter=1000,
    pool_executor_class: type[Executor] = ThreadPoolExecutor,
) -> float:
    logger.info(f"Integrating {n_iter} iters with {n_jobs} jobs and {pool_executor_class.__name__} pool...")
    acc = 0
    step = (b - a) / n_iter

    chunk_size = n_iter // n_jobs
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(n_jobs)]
    chunks[-1] = (chunks[-1][0], n_iter)

    with pool_executor_class(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_chunk, f, chunk, a, step) for chunk in chunks]
        acc = sum(future.result() for future in as_completed(futures))

    logger.info(f"Integrating done, got result: {acc}")
    return acc


def run_for_pool(pool_executor_class: type[Executor], n_jobs_list: list[int]):
    for n_jobs in n_jobs_list:
        t = measure_func(
            lambda: integrate(
                math.cos,
                0,
                math.pi / 2,
                n_jobs=n_jobs,
                n_iter=n_iter,
                pool_executor_class=pool_executor_class,
            )
        )
        print(f"Time for {n_jobs} jobs: {t:.3} seconds")
        n_jobs = math.ceil(n_jobs * 1.5)


print(f"Cpu count is {multiprocessing.cpu_count()}")
n_iter = 30000000
n_jobs_list = [1, 2, 4, 6, 8, 12, 16, 24]
print("Run with ThreadPoolExecutor")
run_for_pool(ThreadPoolExecutor, n_jobs_list)
print("Run with ProcessPoolExecutor")
run_for_pool(ProcessPoolExecutor, n_jobs_list)
