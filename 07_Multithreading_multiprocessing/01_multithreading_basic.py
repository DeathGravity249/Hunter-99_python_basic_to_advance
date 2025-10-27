import threading  # Import the threading module to create and manage threads
import time       # Import the time module to use sleep and track execution time

# Define a function that prints numbers from 0 to 4, with a 2-second delay between each
def print_number():
    for i in range(5):
        time.sleep(2)  # Pause for 2 seconds
        print(f"The numbers are {i}")  # Print the current number

# Define a function that prints letters from 'a' to 'f', with a 2-second delay between each
def print_letter():
    for letter in "abcdef":
        time.sleep(2)  # Pause for 2 seconds
        print(f"The letters are {letter}")  # Print the current letter

# Create a thread object that will run the print_number function in a separate thread
t1 = threading.Thread(target=print_number)

# Create another thread object that will run the print_letter function
t2 = threading.Thread(target=print_letter)

# Record the current time before starting the threads — this marks the start time
t = time.time()

# Start both threads — they will now begin running their target functions at (almost) the same time
t1.start()  # Starts thread t1, which runs print_number
t2.start()  # Starts thread t2, which runs print_letter

# Wait for both threads to complete before moving on
# This ensures the main thread doesn't finish until both t1 and t2 are done
t1.join()
t2.join()

# Calculate how much time has passed since we recorded the start time
# This shows how long both threads took to finish running
finished_time = time.time() - t

# Print the total time taken — should be about 12 seconds (not 22!) because of parallel execution
print(finished_time)
