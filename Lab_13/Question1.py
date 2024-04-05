def IsEmpty(queue):
    return queue == []




def DeQueue(queue):
    # Write your code here
    if IsEmpty(queue):
        return "Priority queue is empty"
    small = queue[0][1]
    data = queue[0][0]
    for i, tup in enumerate(queue):
        if tup[1] < small:
            small = tup[1]
            data = tup[0]
    queue.remove((data, small))
    return data


def EnQueue(queue, item, priority):
    count = 0
    for i, _ in queue:
        if i == item:
            queue[count] = item, priority
            return None
        count += 1
    queue.append((item, priority))

if __name__ == "__main__":
    queue = []
    EnQueue(queue,'A',1)
    EnQueue(queue,'B',2)
    EnQueue(queue,'C',3)
    EnQueue(queue,'D',4)
    EnQueue(queue,'E',5)
    EnQueue(queue,'F',6)
    EnQueue(queue,'G',7)
    print(queue)
    print(DeQueue(queue))
    print(queue)


    

