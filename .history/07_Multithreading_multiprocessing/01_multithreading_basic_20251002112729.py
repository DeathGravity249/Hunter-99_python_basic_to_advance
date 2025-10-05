import threading
import time

def print_number():
    for i in range(5):
        print(f"The numbers are {i}")

def print_letter():
    for letter in "abcdef":
        print(f"The letters are {letter}")

t=time.now()
print_number()
print_letter

finished_time=time.now()


