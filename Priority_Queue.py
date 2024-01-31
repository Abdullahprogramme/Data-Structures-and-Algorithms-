def init(size):
    return {'size': size, 'data': [(10, 10)] * size, 'length': 0}

def isFull(queue):
    return queue['length'] == queue['size']

def isEmpty(queue):
    return queue['length'] == 0

def enqueue(queue, value):
    # Let the priority be the second element in the tuple
    # for example items are: [(1, 3), (2, 4), (3, 4), None, None, None] where size is 6 and length is 3
    flag = False
    if isFull(queue):
        raise IndexError('Queue is full')
    if isEmpty(queue):
        queue['data'][0] = value
        queue['length'] += 1
        flag = True
    
    if flag == False:
        i = 0
        while i < queue['length'] and queue['data'][i][1] <= value[1]:
            i += 1
        for j in range(queue['length'], i, -1):
            queue['data'][j] = queue['data'][j - 1]
        queue['data'][i] = value
        queue['length'] += 1
    
def dequeue(queue):
    if isEmpty(queue):
        raise IndexError('Queue is empty')
    value = queue['data'][0]
    for i in range(1, queue['length']):
        queue['data'][i - 1] = queue['data'][i]
    queue['data'][queue['length'] - 1] = (10, 10)
    queue['length'] -= 1
    return value

# test cases
queue = init(6)
enqueue(queue, (1, 3))
enqueue(queue, (2, 4))
enqueue(queue, (3, 4))
print(queue)
print(isFull(queue))
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
# print(dequeue(queue))
print(queue)
