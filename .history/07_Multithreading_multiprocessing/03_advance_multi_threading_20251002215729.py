### Multipthreading with thread pool executor 

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

numbers=[1,2,3,4,5,6,7,8,9,0,]

with ThreadPoolExecutor(max_workers=3) as executor:
    #“Hey executor! Please take the function print_number() 
    # and apply it to every item in numbers, but do it
    #  using threads (up to max_workers at a time), and give me back the results in order.”
    results=executor.map(print_number,numbers)

for result in results:
    print(result)
## theory behind 

 # ------------------------ Reference Note ------------------------
# This code uses ThreadPoolExecutor for multithreading.
# It processes 10 numbers using a thread pool with max_workers = 3.
#
# Each call to print_number() sleeps for 1 second, simulating a delay.
# Because only 3 threads can run at once, the tasks are processed in batches:
#
# Batch 1: Threads run tasks for 1, 2, 3
# Batch 2: After ~1s, threads are free → run tasks for 4, 5, 6
# Batch 3: After ~2s, run tasks for 7, 8, 9
# Batch 4: After ~3s, last thread runs task for 0
#
# Total time taken ≈ 4 seconds (much faster than sequential: 10 seconds)
#
# Important:
# - ThreadPoolExecutor automatically manages thread creation and queuing
# - executor.map() keeps result order same as input (1,2,3,...0)
# - Best used for I/O-bound tasks (file/network wait, time.sleep, etc.)
#
# For CPU-heavy tasks, consider using ProcessPoolExecutor instead.
# ---------------------------------------------------------------
