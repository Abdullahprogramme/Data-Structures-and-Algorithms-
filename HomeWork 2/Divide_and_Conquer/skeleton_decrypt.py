# Decrypts the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting leaves
# Returns:
#   A tuple containing the original two numbers.
def reverse_karatsuba(data):
    if isinstance(data[0], list):
        data[0] = reverse_karatsuba(data[0]) # recursively call the function if the element is a list
    if isinstance(data[2], list):            # and place the result back where it was called from
        data[2] = reverse_karatsuba(data[2]) # with the result being a tuple

    Num1_Y, Num2_Y = map(str, data[0]) # extract those last two digits of the two numbers to be generated as strings
    Num1_X, Num2_X = map(str, data[2]) # extract those first two digits of the two numbers to be generated as string

    return (int(Num1_X + Num1_Y), int(Num2_X + Num2_Y)) # concatenate the strings and convert them to integer to make the original two numbers

            


# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (x, y).
def main(filename) -> list[tuple[int, int]]:
    result = []
    with open(filename, 'r') as file:
        file_data = int(file.readline().strip())
        for i in range(file_data):
            data = file.readline().strip()
            data, _= make_list(data) # conver the string to list

            # can also use eval(data) but I didn't think of it before
            
            tup = reverse_karatsuba(data) # call the function to decrypt the data
            result.append(tup)
    return result
            
def make_list(s):
    result = []
    i = 0  # Start from the first character
    while i < len(s):
        if s[i] == '[':
            sublist, consumed = make_list(s[i+1:]) # recursively call the function if the element is a list
            result.append(sublist)
            i += consumed + 1
        elif s[i] == '(': # check if the element is a tuple then append it to the list
            pair_end = s.find(')', i)
            pair = tuple(map(int, s[i+1:pair_end].split(',')))
            result.append(pair)
            i = pair_end + 1
        elif s[i] == ']': # if end of list then return the list
            return result, i + 1
        elif s[i] == ',' or s[i] == ' ': # skip the comma and space
            i += 1
        else:
            raise ValueError('Unexpected character: ' + s[i])
    return result[0], i

# print(main("input_decrypt.txt"))