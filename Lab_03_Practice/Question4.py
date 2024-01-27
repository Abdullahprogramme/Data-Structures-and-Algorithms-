from Question2 import *

def InsertAtStart(list, element):
    """
    Insert the given element at the beginning of the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the element into.
    - element: The element to insert at the start of the list.

    Returns:
    str: A string indicating the result of the insertion.
         - "List is full" if the list is already full and no insertion is possible.
         - "Element inserted successfully" if the insertion is successful.
    """
    if IsFull(list): return 'List is full'
    for i in range(Size(list) - 1, 0, -1):
        list[i] = list[i-1]
    list[0] = element
    return 'Element inserted successfully'


if __name__ == "__main__":
    print(InsertAtStart([None,None],'a'))
    ListADT = ["a",None]
    solution = "Element inserted successfully"

    print(InsertAtStart(['a','b'],'c'))
    solution = "List is full"
