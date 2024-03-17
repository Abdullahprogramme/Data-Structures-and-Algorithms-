def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]

def mapping(row, col, row_size):
    return 1 + int((row + row_size * col))

def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    """
    Perform the convolution operation by applying the kernel over the input image.

    Parameter(s):
    - 2D array (int): This is the image on which you have to apply the kernel/filter and perform convolution. 
    - 1D array (int): The first entry in this array is the width of the kernel and the remaining entries are the values of the kernel.

    Returns:
    - 2D array (int): This is the matrix that is obtained after performing convolution.
    """
    Convulated_matrix = init_matrix(len(image), len(image[0]))
    # saving the kernel size up and down
    kernel_half = kernel[0] // 2

    # iterating over each element in the image matrix
    for i in range(len(image)):
        for j in range(len(image[0])):
            neighbours = 0

            # iterating around each element to multiply and sum them
            for row in range(i - kernel_half, i + kernel_half + 1):
                for col in range(j - kernel_half, j + kernel_half + 1):
                    # checking if the elemnt is in the range of the matrix
                    if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]):
                        neighbours += image[row][col] * kernel[int(mapping(row - i + 1, col - j + 1, kernel[0]))]
            Convulated_matrix[i][j] = neighbours
    return Convulated_matrix

def main(file_name: str) -> list[list[int]]:
    """
    The main driver function that will run the entire program. 
    It should extract the image and the kernel from the file and pass them to filter_image(...).

    Parameter(s):
    - file_name (.txt file): Path to a text file that contains the image (2D array) and the kernel (1D array).

    Returns:
    - 2D array (int): This is the matrix that is obtained after executing filter_image(...)
    """

    # Initialize the variables, image and kernel.
    with open(file_name, 'r') as f:
        size = f.readline().strip().split(' ')
        # finding row and column of the matrix
        row, col = int(size[0]), int(size[1])
        image = []
        # finding the matrix
        for i in range(row):
            image.append(list(map(int, f.readline().strip().split(' '))))
        # finding the kernel
        kernel = list(map(int, f.readline().strip().split(' ')))
    f.close()
    # Passing those variables to filter_image
    return filter_image(image, kernel)
