def Initialize(size):
    return {'data': [None] * size, 'top': -1, 'size': size}

def push(lst, val):
    if lst['top'] == lst['size'] - 1:
        raise IndexError("Stack is full")
    lst['top'] += 1
    lst['data'][lst['top']] = val

def pop(lst):
    if lst['top'] == -1:
        raise IndexError("Stack is empty")
    val = lst['data'][lst['top']]
    lst['top'] -= 1
    return val

def peek(lst):
    if lst['top'] == -1:
        raise IndexError("Stack is empty")
    return lst['data'][lst['top']]

def main():
    s = Initialize(5)
    push(s, 1)
    push(s, 2)
    push(s, 3)
    push(s, 4)
    push(s, 5)
    print(pop(s))
    print(pop(s))
    print(pop(s))
    print(pop(s))
    print(pop(s))
    print(pop(s))

if __name__ == "__main__":
    main()