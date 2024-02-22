def Selection_sort(lst):
    for i in range(len(lst) - 1): # n passes
        min = i # n assignments
        for j in range(i+1, len(lst)): # n - i comparisons
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
        
'''
O(n^2) time complexity worst case
O(n) time complexity best case
'''

lst = [6, 4, 9, 2, 3, 1, 5, 8, 7]
Selection_sort(lst)
print(lst)
