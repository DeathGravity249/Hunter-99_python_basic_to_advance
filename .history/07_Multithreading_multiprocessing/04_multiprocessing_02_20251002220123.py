## multiprocessing with process poolexecutor
from concurrent.futures import ThreadPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"square : {number}"