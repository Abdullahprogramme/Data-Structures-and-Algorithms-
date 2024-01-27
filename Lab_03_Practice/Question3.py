from Question1 import *

def Remove(list, index):
    """
    Remove the element at the specified index in the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.
    - index (int): The index of the element to be removed.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Invalid Index" if the provided index is outside the valid range.
         - "Element removed successfully" if the removal is successful.
    """
    if IsEmpty(list): return 'List is empty'
    n = NumberOfElements(list)
    if index < 0 or index >= n: return 'Invalid Index'
    for i in range(index, n - 1):
        list[i] = list[i + 1]
    list[n-1] = None
    # print(list)
    return 'Element removed successfully'


if __name__ == "__main__":
    print(Remove([10, 20, 30, 40, 50], 2))
    ListADT=[10, 20, 40, 50, None]
    solution = "Element removed successfully"

    # print(Remove([10, 20, 40, 50, None], 0))
    # ListADT=[20, 40, 50, None,None]
    # solution = "Element removed successfully"

    # print(Remove([20, 40, 50, None,None], 5))
    # solution = "Invalid Index"

    # print(Remove([None,None,None,None],0))
    # solution= "List is empty"



