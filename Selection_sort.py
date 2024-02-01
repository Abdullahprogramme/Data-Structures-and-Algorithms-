def Selection_sort(lst):
    for i in range(len(lst) - 1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]

lst = [6, 4, 9, 2, 3, 1, 5, 8, 7]
Selection_sort(lst)
print(lst)