def Initialize(n):
    """
    Create and return a new list of size n,
    with all elements initialized to None.

    Parameters:
    - n (int): The size of the list.

    Returns:
    list: A new list with n elements, all set to None.
    """
    return [None for i in range(n)]

def Get(list,index):
    """
    Retrieve the element at the specified index in the list.

    Parameters:
    - list (list): The list to retrieve the element from.
    - index (int): The index of the element to retrieve.

    Returns:
    The element at the specified index in the list.
    """
    return list[index]

def Set(list,index,value):
    """
    Set the element at the specified index in the list to the given value.

    Parameters:
    - list (list): The list to modify.
    - index (int): The index at which to set the value.
    - value: The value to set at the specified index.

    Returns:
    None
    """
    list[index] = value
    

def Size(list):
    """
    Get the size of the list.

    Parameters:
    - list (list): The list to determine the size of.

    Returns:
    int: The size of the list.
    """
    return len(list)

def NumberOfElements(list):
    """
    Get the number of elements in the list.

    Parameters:
    - list (list): The list to count elements in.

    Returns:
    int: The number of elements in the list.
    """
    return len(list) - list.count(None)

def IsEmpty(list):
    """
    Check if the list is empty.

    Parameters:
    - list (list): The list to check.

    Returns:
    bool: True if the list is empty, False otherwise.
    """
    return NumberOfElements(list) == 0

def IsFull(list):
    """
    Check if the list is full.

    Parameters:
    - list (list): The list to check.

    Returns:
    bool: True if the list is full, False otherwise.
    """
    return NumberOfElements(list) == len(list)


if __name__ == "__main__":
    print(Initialize(5))
    solution = [None,None,None,None,None]

    Set([10,None,None,None,None],0,10)
    solution = [10,None,None,None,None]

    print(Get([10,None,None,None,None],0))
    solution = 10

    print(Size([10,None,None,None,None]))
    solution = 5

    print(NumberOfElements([10,None,None,None,None]))
    solution = 1

    print(IsEmpty([10,None,None,None,None]))
    solution = False

    print(IsFull([10,None,None,None,None]))
    solution = False
    