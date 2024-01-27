from Question3 import *

def RemoveFromStart(list):
    """
    Remove the element at the beginning of the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Element removed successfully" if the removal is successful.
    """
    if IsEmpty(list): return 'List is empty'
    n = NumberOfElements(list)
    for i in range(0, n - 1):
        list[i] = list[i + 1]
    list[n-1] = None
    return 'Element removed successfully'


if __name__ == "__main__":
    
    print(RemoveFromStart([None,None]))
    solution = "List is empty"
    print(RemoveFromStart(['a','b']))
    ListADT = ["b",None]
    solution = "Element removed successfully"
