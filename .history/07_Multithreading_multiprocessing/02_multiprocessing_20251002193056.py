## PRocesses theat run in parallel
## CPU-Bound Tasks-Tasks that are heavy on CPU usage (eg,mathematical computation,)
## parallel execution -Multiple core of the CPU

import _multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")

## create 2 processes
p1=_multiprocessing.Process(target=square_numbers)
p2=_multiprocessing.Process(target=cube_numbers)