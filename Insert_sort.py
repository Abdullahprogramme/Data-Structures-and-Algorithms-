def Insert_sort(lst):
    for cn in range(1, len(lst)):
        temp = lst[cn]
        pointer = cn - 1
        while pointer > -1 and lst[pointer] > temp:
            lst[pointer + 1] = lst[pointer]
            pointer -= 1
        lst[pointer + 1] = temp

lst = [6, 4, 9, 2, 3, 1, 5, 8, 7]
Insert_sort(lst)
print(lst)
