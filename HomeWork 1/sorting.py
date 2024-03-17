import math

def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    return [[None for _ in range(n)] for _ in range(n)]


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    count = 0
    for i in arr:
        if i != None:
            count += 1
    return count


def get_maximum(arr: list[int]) -> int:
    """
    A function that takes an array as an argument, and WITHOUT using the built-in functions, returns the maximum value of the array.
    """

    maximum = 0
    for i in arr:
        if i != None:
            if i > maximum:
                maximum = i
    if maximum == 0:
        return None
    return maximum


def insertion_sort(arr: list[int]) -> None:
    """
    A void function that takes a single-dimensional array arr as an argument and applies insertion sort on the valid data items in the array, i.e., the non-None values. This is an in-place function, meaning the original array that was passed as a reference will be updated with the sorted values.
     
    The function should not return anything.
    """
    for i in range(1, length(arr)):
        temp = arr[i]
        pointer = i - 1
        while pointer >= 0 and (arr[pointer] == None or (temp != None and temp < arr[pointer])): # comparision
            arr[pointer + 1] = arr[pointer]
            pointer -= 1
        arr[pointer + 1] = temp
    


def partition_and_prevail(arr: list[int]) -> None:
    """
    A void function that takes the array to be sorted as an argument
    and applies the “Partition and Prevail” algorithm to sort the valid
    data items in the array, as explained in the assignment.

    The function should not return anything.
    """
    maximum = get_maximum(arr) # getting the maximum value
    if maximum != None:
        maximum = int(maximum)

        new_max = maximum + 1
        group_size = math.ceil(new_max / length(arr)) # getting the group size
        matrix = initialize_matrix(group_size) # initializing the matrix

        for item in arr:
            if item == None:
                continue
            row_num = math.ceil(item / group_size)
            row = matrix[row_num]
            for i in range(len(row)):
                if row[i] == None: # inserting the value in the row
                    row[i] = item
                    break  

        # apply insertion sort
        for row in matrix:
            insertion_sort(row) # applying insertion sort on the row

        num = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != None:
                    arr[num] = matrix[i][j]
                    num += 1
    


def main(filename) -> list[int]:
    """
    - Take input from the given filename one line at a time
    - Apply partition_and_prevail sorting algorithm to get the sorted arrays and returns the output as a one dimensional array.
    """
    with open(filename, 'r') as f:
        arr = f.readline().lstrip('[').rstrip(']')
    arr = list(arr.split(', '))
    for i in range(len(arr)):
        if arr[i] == 'None':
            arr[i] = None
        else:  
            arr[i] = int(arr[i])
    partition_and_prevail(arr)
    return arr