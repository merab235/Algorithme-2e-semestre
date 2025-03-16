import time
import tracemalloc
import resource
from lab1.lab_13.src.task13 import can_divide_into_three

def test_time_and_memory():
    values = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]

    tracemalloc.start()
    start_time = time.time()

    result = can_divide_into_three(values)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    usage_after = resource.getrusage(resource.RUSAGE_SELF)
    cpu_time = usage_after.ru_utime
    memory_usage = usage_after.ru_maxrss

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")
    print(f"CPU time used: {cpu_time:.6f} seconds")
    print(f"Max RSS memory: {memory_usage} KB")

test_time_and_memory()
