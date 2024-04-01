from multiprocessing import Process
from threading import Thread

from hw_4.measure import measure_func


def fibonacci(n: int) -> int:
    x, y = 0, 1
    for _ in range(1, n):
        x, y = y, x + y
    return y


def sync_run(times: int, n: int):
    for i in range(times):
        fibonacci(n)


def threads_run(times: int, n: int):
    threads = [Thread(target=fibonacci, args=(n,)) for _ in range(times)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def processes_run(times: int, n: int):
    processes = [Process(target=fibonacci, args=(n,)) for _ in range(times)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


n = 300000
times = 10
print(f"Evaluating {n}'th fibonacci number {times} times")
t = measure_func(lambda: sync_run(times, n))
print(f"Sync time: {t:.3} seconds")

t = measure_func(lambda: threads_run(times, n))
print(f"Threads time: {t:.3} seconds")

t = measure_func(lambda: processes_run(times, n))
print(f"Processes time: {t:.3} seconds")
