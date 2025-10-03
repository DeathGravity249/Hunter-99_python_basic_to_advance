## multiprocessing with process poolexecutor
from concurrent.futures import ThreadPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"square : {number*number}"

numbers=[11,22,33,44,55,66,63,74,77,99,93]

with ThreadPoolExecutor