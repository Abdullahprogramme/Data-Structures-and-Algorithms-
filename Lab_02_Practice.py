def initialize_matrix(rows, cols):
    return [[0 for i in range(cols)] for j in range(rows)]

def matrix_subtraction(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]): return "Size not same"
    else:
        new = initialize_matrix(len(A), len(A[0]))
        for row in range(len(A)):
            for column in range(len(B[0])): 
                new[row][column] = A[row][column] - B[row][column]
        return new

def Transpose(A):
    new = initialize_matrix(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            new[col][row] = A[row][col]
    return new

def matrix_multiplication(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]): return "Size not same"
    else:
        new = initialize_matrix(len(A), len(B[0]))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    new[i][j] += A[i][k] * B[k][j]
        return new

def size_reduction(A):
    new = initialize_matrix(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            a = sum( A[i][j] for i in range(row-1,row+2) for j in range(col-1,col+2) if (0 <= i < len(A)) and (0 <= j < len(A[0])) )
            new[row][col] = round(((a - A[row][col]) * A[row][col]) ** (1/3), 3)
    return new
print(size_reduction([[1,2,3], [4,5,6], [7,8,9]]))