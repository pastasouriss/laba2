def find_min_index(matrix):
    min_value = float('inf')
    min_row = -1
    min_col = -1

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_row = i
                min_col = j

    return min_row, min_col
def find_max_index(matrix):
    max_value = float('-inf')
    max_row = -1
    max_col = -1

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_row = i
                max_col = j

    return max_row, max_col
matrix = [
    [1, 2, 3],
    [0, 9, 6],
    [7, 8, 4]
]
min_index = find_min_index(matrix)
print("Индексы первого вхождения минимального элемента:", min_index)

max_index = find_max_index(matrix)
print("Индексы наибольшего элемента:", max_index)