from Question1 import *

def Insert(list,index,value):
    """
    Insert the given value at the specified index in the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the value into.
    - index (int): The index at which to insert the value.
    - value: The value to insert into the list.

    Returns:
    str: A string indicating the result of the insertion.
        - "List is full" if the list is already full and no insertion is possible.
        - "Invalid Index" if the provided index is outside the valid range.
        - "Element inserted successfully" if the insertion is successful.
    """
    if IsFull(list): return 'List is full'
    elif index < 0 or index >= Size(list): return 'Invalid Index'
    for i in range(Size(list) - 1, index, -1):
        list[i] = list[i - 1]
    list[index] = value
    return "Element inserted successfully"

if __name__ == "__main__":
    Insert([None,None,None],0,'a')
    solution = "Element inserted successfully"
    ListADT = ["a",None,None]
    
    print(Insert(["a",None,None],1,'b'))
    ListADT = ["a","b",None]
    solution = "Element inserted successfully"

    print(Insert(["a","b",None],4,'e'))
    solution = "Invalid Index"

    print(Insert(["a","b",None],2,'c'))
    ListADT = ["a","b","c"]
    solution ="Element inserted successfully"

    print(Insert(["a","b","c"],3,'d'))
    solution="List is full"