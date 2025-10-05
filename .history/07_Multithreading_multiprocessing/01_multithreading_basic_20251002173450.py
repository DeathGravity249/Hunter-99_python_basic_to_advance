import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"The numbers are {i}")

def print_letter():
    for letter in "abcdef":
        time.sleep(2)
        print(f"The letters are {letter}")

t1=threading.Thread(target=print_number) 
## It just prepare the thread not yet calling
t2=threading.Thread(target=print_letter)

t=time.time()
#start the thread
t1.start()
t2.start()

## Wait for the threads to complete
t1.join()
t2.join()

# print_number()
# print_letter()

finished_time=time.time()-t
print(finished_time)


