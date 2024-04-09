def create_hashtable(size): # returns tuple(list,list)
    return ([None] * size, [None] * size)

def find_next_prime(size): # returns integer
    prime = 0
    for i in range(size+1, 2*size): # iterate from that number to its double as the new prime will be their
        for j in range(2, i):
            if i % j != 0:
                prime = i # only set prime to i if i is not divisible by any number other than 1 and itself
            else:
                prime = 0
                break
        if prime != 0:
            break
        
    return prime

def resize_hashtable(hashtable,size,increase): #return hashtable,size
    # primes = [3, 5, 7, 11, 17, 23, 47, 97, 197, 397, 797, 1597, 3203, 6421, 12853, 25717, 51437, 102877, 205759] # prime numbers
    if increase == True: # if increase is True, double the size of hashtable
        size = size * 2
        size = find_next_prime(size) # find the next prime number greater than the new size

    else: # if increase is False, half the size of hashtable
        size = size // 2
        size = find_next_prime(size) # find the next prime number greater than the new size
        if size < 7: # if size is less than 7, set size to 7
            size = 7

    keys, values = hashtable # get the keys list and values list from the hashtable
    new_hashtable = create_hashtable(size) # create a new hashtable with the new size
    for key, value in zip(keys, values): # iterate through the keys and values lists
        # print(key)
        if key is not None and key != '#': # the key should not be None or '#'
            index = hash_function(key, size) # get the index of the key in the new hashtable
            if new_hashtable[0][index] is None: # directly insert the key and value if the index is empty
                new_hashtable[0][index] = key
                new_hashtable[1][index] = value
            else: # if the index is not empty, resolve the collision
                while new_hashtable[0][index] is not None:
                    index = collision_resolver(key, index, size) # call the collision_resolver until an empty index is found
                new_hashtable[0][index] = key
                new_hashtable[1][index] = value
    return new_hashtable, size


def hash_function(key,size): #returns integer (Address)
    val = sum(ord(char) for char in key) # sum of the ASCII values of the characters in the key
    val = val >> 4 # right shift by 4 bits
    val = val % size
    return val if val >= 0 else -val # make it positive if it is negative by multiplying by -1


def collision_resolver(key,oldAddress,size): #returns integer (Address)
    offset = sum(ord(char) for char in key) // size # sum the ASCII values of the characters
    address = (oldAddress + offset) % size
    return address

def put(hashtable,key, data,size): #return hashtable,size
    val = loadFactor(hashtable,size) # get the load factor of the hashtable

    if val > 0.75:
        hashtable, size = resize_hashtable(hashtable, size, True) # if the load factor is greater than 0.75, double the size of the hashtable
    index = hash_function(key, size) # get the index of the key to be inserted

    keys, values = hashtable
    # print(key, index, size, len(keys))
    if keys[index] is None and key[index] != '#': # diretly insert the key and value if the index is empty
        keys[index] = key
        values[index] = data
    else:
        while keys[index] is not None and keys[index] != '#': # else resolve the collision
            index = collision_resolver(key, index, size)
        keys[index] = key
        values[index] = data
        
    return (keys, values), size


def loadFactor(hashtable,size): # returns a float - Loadfactor of hashtable
    keys, values = hashtable
    count = 0
    for key in keys: # count the non-empty keys in the keys list
        if key is not None and key != '#': # check if the key is not None or '#' since they both mean that there is no key at that index
            count += 1
    return count / size

def Update(hashtable,key, columnName, data,size,collision_path,opNumber): # returns Nothing, prints 'record Updated'
    keys, values = hashtable

    collision_path[opNumber] = [] # create a list in the collision_path dictionary with the opNumber as the key

    index = hash_function(key, size)
    collision_path[opNumber].append(index) # append the index to the list in the collision_path dictionary 
    if keys[index] == key: # if the key is found at the index, update the value at that specific column
        values[index][columnName] = data
        print('record Updated')
    else:
        while keys[index] is not None and keys[index] != '#': # else resolve the collision
            index = collision_resolver(key, index, size)
            collision_path[opNumber].append(index) # append the index to the list in the collision_path dictionary
            if keys[index] == key:
                values[index][columnName] = data # update the value
                print('record Updated')
                break
        
    
def get(hashtable,key,size,collision_path,opNumber): # returns dictionary
    keys, values = hashtable

    collision_path[opNumber] = [] # create a list in the collision_path dictionary with the opNumber as the key

    index = hash_function(key, size)
    collision_path[opNumber].append(index) # append the index to the list in the collision_path dictionary 
    if keys[index] == key: # if the key is found at the index, return the value
        return values[index]
    else:
        index = collision_resolver(key, index, size)   
        collision_path[opNumber].append(index) # append the index to the list in the collision_path dictionary 
        while keys[index] is not None and keys[index] != '#': # resolve the collision until you find the key
            if keys[index] == key: # if the key is found, return the value
                return values[index]
            index = collision_resolver(key, index, size)
            collision_path[opNumber].append(index) # append the index to the list in the collision_path dictionary
    return 'Item not found' # if the key is not found, return 'Item not found'
        
def delete(hashtable, key, size, collision_path,opNumber): #returns hashtable, size, prints a msg  'Item Deleted'
    val = loadFactor(hashtable,size) # get the load factor of the hashtable

    # if val > 0.75:
    #     hashtable, size = resize_hashtable(hashtable, size, True) # if the load factor is greater than 0.75, double the size of the hashtable
    if val < 0.3 and size > 7:
        hashtable, size = resize_hashtable(hashtable, size, False) # if the load factor is less than 0.3 and the size is greater than 7, half the size of the hashtable
    
    keys, values = hashtable

    collision_path[opNumber] = [] # create a list in the collision_path dictionary with the opNumber as the key

    index = hash_function(key, size)
    collision_path[opNumber].append(index) # append the index to the list in the collision_path dictionary
    if keys[index] == key:  # if the key is found at the index, delete the key and value
        keys[index] = '#'
        values[index] = '#' 
        print('Item Deleted')
    else:
        while keys[index] is not None and keys[index] != '#': # else resolve the collision
            index = collision_resolver(key, index, size)
            collision_path[opNumber].append(index)
            if keys[index] == key:
                keys[index] = '#'
                values[index] = '#'
                print('Item Deleted')
                break
    return (keys, values), size