import time
import tracemalloc
from lab1.lab_15.src.task15 import remove_invalid_brackets

def test_remove_parentheses():
    s = "({[]})" * 1000  

    
    tracemalloc.start()

    
    start_time = time.time()

    result = remove_invalid_brackets(s)

    
    end_time = time.time()

    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    
    print(f"Execution time for exercise 15: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")


test_remove_parentheses()