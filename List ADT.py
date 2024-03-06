# def initialize(size):
#     return {'data': [None] * size, 'size': size, 'length': 0, 'i': 0}

# def is_empty(list):
#     return list['length'] == 0

# def is_full(list):
#     return list['length'] == list['size']

# def get(list, index):
#     if index < 0 or index >= list['length']:
#         raise IndexError('Index is out of bounds')
#     return list['data'][index]

# def set(list, index, value):
#     if index < 0 or index >= list['length']:
#         raise IndexError('Index is out of bounds')
#     list['data'][index] = value

# def length(list):
#     return list['length']

# def insert(list, index, value):
#     if is_full(list):
#         raise IndexError('List is full')
#     if index < 0 or index > list['length']:
#         raise IndexError('Index is out of bounds')
#     for i in range(list['length'], index, -1):
#         list['data'][i] = list['data'][i - 1]
#     list['data'][index] = value
#     list['length'] += 1

# def remove(list, index):
#     if is_empty(list):
#         raise IndexError('List is empty')
#     if index < 0 or index >= list['length']:
#         raise IndexError('Index is out of bounds')
#     value = list['data'][index]
#     for i in range(index, list['length'] - 1):
#         list['data'][i] = list['data'][i + 1]
#     list['length'] -= 1
#     return value

# def insert_last(list, value):
#     if is_full(list):
#         raise IndexError('List is full')
#     i = list['i']
#     n = list['length']
#     s = list['size']
#     list['data'][(i + n) % s] = value
#     list['length'] += 1

# def remove_last(list):
#     if is_empty(list):
#         raise IndexError('List is empty')
#     i = list['i']
#     n = list['length']
#     s = list['size']
#     value = list['data'][(i + n) % s]
#     list['length'] -= 1
#     return value

# def insert_first(list, value):
#     if is_full(list):
#         raise IndexError('List is full')
#     i = list['i']
#     s = list['size']
#     list['i'] = (s - 1) if i - 1 < 0 else (i - 1)
#     list['data'][i] = value
#     list['length'] += 1

# def remove_first(list):
#     if is_empty(list):
#         raise IndexError('List is empty')
#     i = list['i']
#     s = list['size']
#     value = list['data'][i % s]
#     list['i'] = (i + 1) % s
#     list['length'] -= 1
#     return value

# def get_first(list):
#     if is_empty(list):
#         raise IndexError('List is empty')
#     i = list['i']
#     s = list['size']
#     return list['data'][(i + 1) % s]

# def get_last(list):
#     if is_empty(list):
#         raise IndexError('List is empty')
#     i = list['i']
#     n = list['length']
#     s = list['size']
#     return list['data'][(i + n) % s]

# l = initialize(5)
# print(l)
# insert_last(l, 1)
# print(l)
# item = remove_first(l)
# print(l, item)
# insert_first(l, 2)
# print(l)

def initialize(size):
    return {'data': [None] * size, 'size': size, 'length': 0, 'i': 0}

def is_empty(list):
    return list['length'] == 0

def is_full(list):
    return list['length'] == list['size']

def get(list, index):
    if index < 0 or index >= list['length']:
        raise IndexError('Index is out of bounds')
    return list['data'][index]

def set(list, index, value):
    if index < 0 or index >= list['length']:
        raise IndexError('Index is out of bounds')
    list['data'][index] = value

def length(list):
    return list['length']

def insert(list, index, value):
    if is_full(list):
        raise IndexError('List is full')
    if index < 0 or index > list['length']:
        raise IndexError('Index is out of bounds')
    for i in range(list['length'], index, -1):
        list['data'][i] = list['data'][i - 1]
    list['data'][index] = value
    list['length'] += 1

def remove(list, index):
    if is_empty(list):
        raise IndexError('List is empty')
    if index < 0 or index >= list['length']:
        raise IndexError('Index is out of bounds')
    value = list['data'][index]
    for i in range(index, list['length'] - 1):
        list['data'][i] = list['data'][i + 1]
    list['length'] -= 1
    return value

def insert_last(list, value):
    if is_full(list):
        raise IndexError('List is full')
    i = list['i']
    n = list['length']
    s = list['size']
    list['data'][(i + n) % s] = value
    list['length'] += 1

def remove_last(list):
    if is_empty(list):
        raise IndexError('List is empty')
    i = list['i']
    n = list['length']
    s = list['size']
    value = list['data'][(i + n - 1) % s]
    list['length'] -= 1
    return value

def insert_first(list, value):
    if is_full(list):
        raise IndexError('List is full')
    i = list['i']
    s = list['size']
    list['i'] = (i - 1 + s) % s 
    list['data'][list['i']] = value
    list['length'] += 1

def remove_first(list):
    if is_empty(list):
        raise IndexError('List is empty')
    i = list['i']
    s = list['size']
    value = list['data'][i]
    list['i'] = (i + 1) % s
    list['length'] -= 1
    return value

def get_first(list):
    if is_empty(list):
        raise IndexError('List is empty')
    i = list['i']
    s = list['size']
    return list['data'][(i + 1) % s]

def get_last(list):
    if is_empty(list):
        raise IndexError('List is empty')
    i = list['i']
    n = list['length']
    s = list['size']
    return list['data'][(i + n) % s]

l = initialize(5)
print(l)
insert_first(l, 1)
print(l)
insert_last(l, 2)
print(l)
insert_first(l, 3)
print(l)
insert_last(l, 4)
print(l)
val = remove_first(l)
print(val, l)
val = remove_last(l)
print(val, l)
val = remove_first(l)
print(val, l)
val = remove_last(l)
print(val, l)
