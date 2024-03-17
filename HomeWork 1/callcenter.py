# DO NOT CHANGE THIS FUNCTION
# Create a basic queue
def create_queue(size: int) -> dict:
    """
    Description: Creates and initializes a basic queue with a specified size.
    Parameters: size - an integer representing the size of the queue.
    Return: A dictionary representing the initialized queue.
    """
    return {
        'data': [None] * size,  # list of elements
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# DO NOT CHANGE THIS FUNCTION
# Create a priority queue
def create_priority_queue(size: int) -> dict:
    """
    Description: Creates and initializes a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: size - an integer representing the size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    return {
        'data': [(None, float('inf'))] * size,  # list of elements with default priority set to infinity
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# Check if the queue is full
def is_full(queue: dict) -> bool:
    """
    Description: Checks if the given queue is full (reached its maximum capacity).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is full, False otherwise.
    """
    return queue['n'] == queue['size']

# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    """
    Description: Checks if the given queue is empty (contains no elements).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is empty, False otherwise.
    """
    return queue['n'] == 0

# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    """
    Description: Adds an element with the value 'val' to the rear of the queue.
    Parameters: queue - a dictionary representing the queue, val - the value to be added to the queue.
    """
    if is_full(queue):
        return
    if queue['rear'] == -1: 
        queue['front'] = 0
    queue['rear'] = (queue['rear'] + 1) % queue['size'] # incrementing the rear pointer
    queue['data'][queue['rear']] = item # adding the element to the rear of the queue
    queue['n'] += 1


# Remove and return the element from the front of the queue
def dequeue(queue: dict) :
    """
    Description: Removes and returns the element from the front of the queue.
    Parameters: queue - a dictionary representing the queue.
    Return: The element from the front of the queue.
    """
    if is_empty(queue):
        raise ValueError('Queue is empty')
    item = queue['data'][queue['front']] # get the front element
    queue['front'] = (queue['front'] + 1) % queue['size'] # incrementing the front pointer
    queue['n'] -= 1 
    return item


# Return the element at the front of the queue without removing it
def peek(queue: dict):
    """
    Description: Returns the element at the front of the queue without removing it.
    Parameters: queue - a dictionary representing the queue.
    Return: The element at the front of the queue.
    """
    if is_empty(queue):
        raise ValueError('Queue is empty') # raise an error if the queue is empty
    return queue['data'][queue['front']] # return the front element

# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    """
    Description: Adds an element with the value 'val' and the specified priority to the priority queue.
    Parameters: queue - a dictionary representing the priority queue, val - the value to be added to the queue,
                priority - the priority of the element.
    """
    if is_full(priority_queue): # raise an error if the priority queue is full
        raise ValueError('Priority queue is full')
    if is_empty(priority_queue): # if the priority queue is empty, add the element at index 0
        priority_queue['data'][0] = (item, priority)
    else: 
        i = 0
        while i < priority_queue['n'] and priority_queue['data'][i][1] <= priority: # find the minimum priority
            i += 1
        for j in range(priority_queue['n'], i, -1):
            priority_queue['data'][j] = priority_queue['data'][j - 1] # shift the elements to the right
        priority_queue['data'][i] = (item, priority) # add the element at the correct position
        # if item != None:
    priority_queue['n'] += 1
         

# Remove and return the element with the minimum priority from the priority queue
def dequeue_min_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    if is_empty(priority_queue):
        raise ValueError('Priority queue is empty') # raise an error if the priority queue is empty
    value = priority_queue['data'][0]
    for i in range(1, priority_queue['n']):
        priority_queue['data'][i - 1] = priority_queue['data'][i]
    # priority_queue['data'][priority_queue['n'] - 1] = (None, float('inf'))
    priority_queue['n'] -= 1
    return value

# Return the element with the minimum priority from the priority queue without removing it
def peek_min_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    return priority_queue['data'][0] # return the element with the minimum priority

def CallSimulator(callQueue, agentQueue) -> dict:
    """
    Description: Simulates a call center scenario where calls are processed by agents based on their availability.
    Type: Function
    Parameters: callQueue - a dictionary representing the call queue,
                AgentQueue - a dictionary representing the agent queue.
    Return: A queue containing information about each processed call (callerName, call_start, call_end, wait_time).
    """
    # Simulation parameters
    Simulation = True
    currentTime = 0

    # Create a queue to store the call log
    callLog = create_queue(callQueue['size'])

    
    while Simulation:
        # provide your implementation here

        while not is_empty(callQueue):
            if peek(callQueue)[0] <= currentTime and peek_min_priority(agentQueue)[1] <= currentTime and not is_empty(agentQueue):

                    # dequeueing the call
                    call = dequeue(callQueue)
                    start_time, customer, duration = call
                    
                    # dequeueing the agent with the minimum priority
                    agent, priority = dequeue_min_priority(agentQueue)

                    wait_time = currentTime - start_time # calculating the wait time

                    # adding the call log to the call log queue and adding the agent back to the agent queue
                    enqueue(callLog, (customer, currentTime, currentTime + duration, wait_time))
                    enqueue_priority(agentQueue, agent, currentTime + duration)
            else:
                currentTime += 1

            if is_empty(callQueue): # if the call queue is empty, stop the simulation
                Simulation = False

        # if is_empty(callQueue): # if the call queue is empty, stop the simulation
        #     Simulation = False
        
        # Increment the current time for the next iteration
        # currentTime += 1
    
    # Returning the queue containing the call log
    return callLog


def main(filename) -> list:
    """
    Description: Main function to read input data from a file, initialize agent and call queues, simulate call processing using CallSimulator, and return the call log data.
    Parameters: filename - the name of the file containing input data.
    Return: A list representing the call log data.
    """
    
    # Read input data from the file
    # First line contains the list of agents separated by spaces 
    # Second line contains the number of calls to be processed
    # Populate the call queue with call details from the remaining lines contain the call details (start time, caller name, call duration) separated by spaces

    # provide your implementation here 
    with open(filename, 'r') as f:
        data = f.readline()
        agents = data.strip().split(' ')
        number = int(f.readline().strip())

        # creating the agent and call queues
        agentQueue = create_priority_queue(len(agents))
        call_queue = create_queue(number)
        for agent in agents: # adding the agents to the agent queue
            enqueue_priority(agentQueue, agent, 0)
        for i in range(number):
            call = f.readline()
            arrival_time, customer, duration = call.strip().split(' ') # adding the calls to the call queue
            enqueue(call_queue, (int(arrival_time), customer, int(duration)))

    # Simulate call processing using CallSimulator
    call_log = CallSimulator(call_queue, agentQueue)
    
    # Return the call log data as a list
    return call_log['data']
