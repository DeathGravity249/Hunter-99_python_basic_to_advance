import multiprocessing
import math
import sys
import time

## increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## fuction to compute the factorial of a given number 

def computer_factorial(number):
    print(f"computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")