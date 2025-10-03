## multiprocessing with process poolexecutor
from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"square : {number*number}"

t=time.time()
numbers=[11,22,33,44,55,66,63,74,77,99,93]

with ProcessPoolExecutor(max_workers=3) as executor:
    results=executor.map(square_number,numbers)

for result in results:
    print