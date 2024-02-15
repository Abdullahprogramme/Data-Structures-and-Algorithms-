def Quick_sort(A, lb, ub):
    if lb < ub:
        pivot = Partition(A, lb, ub)
        Quick_sort(A, lb, pivot - 1)
        Quick_sort(A, pivot + 1, ub)
    
def Partition(A, lb, ub):
    pivot = A[lb]
    start = lb
    end = ub
    while start < end:
        while A[start] <= pivot:
            start += 1
        while A[end] > pivot:
            end -= 1
        if start < end:
            A[start], A[end] = A[end], A[start]
    A[lb], A[end] = A[end], A[lb]
    return end

A = [5, 3, 8, 4, 2, 7, 1, 10]
Quick_sort(A, 0, len(A) - 1)
print(A)