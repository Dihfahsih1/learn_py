import threading

# Define a function that will be executed in a separate thread
def thread_function():
    for i in range(5):
        print("Thread execution:", i)

# Create a new thread
thread = threading.Thread(target=thread_function)

# Start the thread
thread.start()

# The main thread continues to execute concurrently with the new thread
for i in range(5):
    print("Main execution:", i)

# Wait for the thread to finish
thread.join()

# The main thread resumes after the other thread has finished
print("Program completed")
