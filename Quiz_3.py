def Unimodal_search(matrix):
    val = 0
    for i in range(len(matrix)):
        low = 0
        high = len(matrix[i]) - 1
        flag = False
        while low < high and flag == False:
            mid = (low + high) // 2
            if matrix[i][mid - 1] < matrix[i][mid] and matrix[i][mid + 1] < matrix[i][mid]:
                # print(matrix[i][mid])
                if matrix[i][mid] > val:
                    val = matrix[i][mid]
                flag = True
            elif matrix[i][mid - 1] < matrix[i][mid] and matrix[i][mid + 1] > matrix[i][mid]:
                low = mid
            else:
                high = mid
    return val

matrix = [[-23, -8, -3, 0, 3, 2, 1], [-20, -7, -2, 1, 4, 3, 2], [-18, -5, 0, 3, 6, 5, 4], [-100, -90, 56, 57, 58, 59, 1]]
print(Unimodal_search(matrix))