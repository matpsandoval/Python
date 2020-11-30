import os

file_dir = os.path.dirname(__file__)
file_try = open(os.path.join(file_dir, "try.txt"))

sudoku = file_try.read().split()


def contains_duplicates(list):
    set_list = set(list)
    return len(set_list) != len(list)


for index in range(9):
    start_index = index * 9
    end_index = start_index + 9

    row = sudoku[start_index : end_index]
    result = contains_duplicates(row)

    print("row has duplicates?:", result, row)

for index in range(9):
    column = []

    for x in range(9):
        element_index = (x * 9) + index
        column.append(sudoku[element_index])

    result = contains_duplicates(column)

    print("column has duplicates?:", result, column)

        
for index in range(9):
    block = []

    index_range = index // 3
    start_index = index_range * 27

    extract_position = (index) - (index_range * 3)

    pointer = start_index + (3 * extract_position)

    for x in range(3):
        start_block_index = (x * 9) + pointer
        file_block = sudoku[start_block_index : start_block_index + 3]

        block.extend(file_block)

    result = contains_duplicates(block)

    print("block has duplicates?:", result, block)