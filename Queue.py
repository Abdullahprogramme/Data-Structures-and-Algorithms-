def Initialize(size):
    return {'data': [None] * size, 'rear': 0, 'front': 0, 'size': size}

def enQueue(lst, val):
    if lst['rear'] != lst['size'] - 1:
        raise IndexError("Stack is full")
    lst['data'][lst['rear']] = val
    lst['rear'] += 1

def deQueue(lst):
    if lst['rear'] == lst['front']:
        raise IndexError("Stack is empty")
    val = lst['data'][lst['rear']]
    lst['rear'] -= 1
    return val

def peek(lst):
    if lst['rear'] == lst['front']:
        raise IndexError("Stack is empty")
    return lst['data'][lst['front']]

def main():
    q = Initialize(5)
    enQueue(q, 1)
    enQueue(q, 2)
    enQueue(q, 3)
    enQueue(q, 4)
    enQueue(q, 5)
    print(deQueue(q))
    print(deQueue(q))
    print(deQueue(q))
    print(deQueue(q))
    print(deQueue(q))
    print(deQueue(q))

if __name__ == "__main__":
    main()