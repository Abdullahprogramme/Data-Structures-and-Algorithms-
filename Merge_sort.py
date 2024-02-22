def merge(A, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    
def Merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        Merge_sort(left)
        Merge_sort(right)
        merge(A, left, right)
        
'''
# O(nlogn) time complexity
'''
    
A = [5, 3, 8, 4, 2, 7, 1, 10]
Merge_sort(A)
print(A) # [1, 2, 3, 4, 5, 7, 8, 10]
