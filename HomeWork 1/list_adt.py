def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """
    return {'size': size, 'data': [None] * size, 'n': 0, 'i': 0}

def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    return listADT['messages']['n'] == 0

def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    return listADT['messages']['n'] == listADT['messages']['size']

def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    return listADT['messages']['data'][(listADT['messages']['i'] + i) % listADT['messages']['size']]

def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    listADT['messages']['data'][(listADT['messages']['i'] + i) % listADT['messages']['size']] = e

def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    return listADT['messages']['n']

def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        raise Exception('Deque is full')
    if i < 0 or i > listADT['messages']['size']:
        raise Exception('Invalid index')
    # for i in range(listADT['n'], i, -1):
    #     listADT['messages'][i] = listADT['messages'][i - 1]
    # listADT['messages'][i] = e
    # listADT['n'] += 1
    listADT['messages']['data'][listADT['messages']['i']] = tuple(e)
    listADT['messages']['i'] = (listADT['messages']['i'] + 1) % listADT['messages']['size']
    listADT['messages']['n'] += 1

def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        raise Exception('Deque is empty')
    if i < 0 or i >= listADT['messages']['size']:
        raise Exception('Invalid index')
    e = listADT['messages']['data'][i]
    for i in range(i, listADT['n'] - 1):
        listADT['messages']['data'][i] = listADT['messages']['data'][i + 1]
    listADT['messages']['data'][listADT['n'] - 1] = None
    listADT['n'] -= 1
    
    return e

def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        raise Exception('Deque is full')
    listADT['messages']['data'][(listADT['messages']['i'] + listADT['messages']['n']) % listADT['messages']['size']] = e
    listADT['n'] += 1
    

def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        raise Exception('Deque is empty')
    # e = listADT['messages'][(listADT['i'] + listADT['n']) % listADT['size']]
    # listADT['n'] -= 1
    listADT['messages']['data'][listADT['messages']['i'] - 1] = None
    listADT['messages']['i'] = (listADT['messages']['i'] - 1) % listADT['messages']['size']
    listADT['messages']['n'] -= 1

def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        raise Exception('Deque is full')
    listADT['i'] = (listADT['messages']['size'] - 1) if listADT['messages']['i'] - 1 < 0 else (listADT['messages']['i'] - 1)
    listADT['messages']['data'][listADT['messages']['i']] = e
    listADT['messages']['n'] += 1

def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        raise Exception('Deque is empty')
    e = listADT['messages']['data'][listADT['messages']['i'] % listADT['messages']['size']]
    listADT['messages']['i'] = (listADT['messages']['i'] + 1) % listADT['messages']['size']
    listADT['messages']['n'] -= 1
    
    return e

def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    if is_empty(list):
        raise IndexError('List is empty')
    i = listADT['messages']['i']
    s = listADT['messages']['size']
    return listADT['messages']['data'][(i + 1) % s]

def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    if is_empty(list):
        raise IndexError('List is empty')
    i = listADT['messages']['i']
    n = listADT['messages']['n']
    s = listADT['messages']['size']
    return listADT['messages']['data'][(i + n) % s]
