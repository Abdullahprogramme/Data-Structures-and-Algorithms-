def farm(field, num_iterations=3):
    harvested = 0
    for _ in range(num_iterations):
        row_index, sum_row, col_index, sum_col = find_max_sum_coordinates(field)
        print(sum_row, sum_col)
        if sum_row > sum_col:
            for col in range(len(field[0])):
                harvested += field[row_index][col]
                field[row_index][col] = 0
        else:
            for row in range(len(field)):
                harvested += field[row][col_index]
                field[row][col_index] = 0
    return harvested

def find_max_sum_coordinates(field):
    row_index = col_index = sum_row = sum_col = 0

    # Row summing up
    for i in range(len(field)):
        total = sum(field[i])
        if total > sum_row:
            sum_row = total
            row_index = i

    # Column summing up
    for col in range(len(field[0])):
        total = sum(field[row][col] for row in range(len(field)))
        if total > sum_col:
            sum_col = total
            col_index = col

    return row_index, sum_row, col_index, sum_col

a = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6]
]

print(farm(a))
