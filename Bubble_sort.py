def Bubble_sort(lst):
    flag = False
    while flag == False:
        flag = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = False

lst = [6, 4, 9, 2, 3, 1, 5, 8, 7]
Bubble_sort(lst)
print(lst)

def inefficient_bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

lst = [6, 4, 9, 2, 3, 1, 5, 8, 7]
inefficient_bubble_sort(lst)
print(lst)
