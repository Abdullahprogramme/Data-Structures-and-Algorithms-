def Insert_sort(lst):
    for cn in range(1, len(lst)): # n + 1 passes
        temp = lst[cn] # n assignments
        pointer = cn - 1 # n assignments
        while pointer > -1 and lst[pointer] > temp: # n + n comparisons
            lst[pointer + 1] = lst[pointer] # n assignments
            pointer -= 1 # n assignments
        lst[pointer + 1] = temp # n assignments
    
'''
O(n^2) time complexity 
'''
        
lst = [6, 4, 9, 2, 3, 1, 5, 8, 7]
Insert_sort(lst)
print(lst)
