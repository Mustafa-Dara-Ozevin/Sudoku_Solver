import random
import copy


def format(sudoku):
    sudoku_formatted = sudoku
    for row in range(len(sudoku_formatted)):
        for i in [3, 7]:
            sudoku_formatted[row].insert(i, '|')

        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - - - - - - - ')
        print(sudoku_formatted[row])


def is_grid_full(sudoku_grid):
    for row in range(9):
        for column in range(9):
            if sudoku_grid[row][column] == 0:
                return False
    return True


def find_empty_square(sudoku):
    for row in range(len(sudoku)):
        for column in range(len(sudoku[row])):
            if sudoku[row][column] == 0:
                return row, column


def check_square(number, row_index, column_index, sudoku):
    checked_number = number
    # check on row
    for number in sudoku[row_index]:
        if number == checked_number:
            return False

    # check on column
    for row in sudoku:
        if row[column_index] == checked_number:
            return False

    # check on square
    square_row = round(row_index/3-0.3)
    square_column = round(column_index/3-0.3)
    for row in range(square_row*3, square_row*3+3):
        for column in range(square_column*3, square_column*3+3):
            if sudoku[row][column] == checked_number:
                return False
    return True


def solve_sudoku(sudoku):
    global counter
    find = find_empty_square(sudoku)
    if not find:
        return True
    row_index, column_index = find
    for i in range(1, 10):
        if check_square(i, row_index, column_index, sudoku):
            sudoku[row_index][column_index] = i

            if is_grid_full(grid):
                counter += 1
                break
            else:
                if solve_sudoku(sudoku):
                    return True

            sudoku[row_index][column_index] = 0

    return False


def create_empty_grid():
    empty_grid = []
    for x in range(9):
        empty_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    return empty_grid


def fill_grid(grid):
    number_list = list(range(1, 10))
    find = find_empty_square(grid)
    if not find:
        return True
    row, column = find
    random.shuffle(number_list)
    for number in number_list:
        if check_square(number, row, column, grid):
            grid[row][column] = number

            if fill_grid(grid):
                return True

            grid[row][column] = 0
    return False

    if not is_grid_full(grid):
        solve_sudoku(grid)
    return True


def remove_numbers_from_grid(grid):
    global counter
    attempts = 1
    counter = 1
    while attempts > 0:
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if grid[row][column] != 0:
            deleted_number = grid[row][column]
            grid[row][column] = 0

            grid_copy = copy.deepcopy(grid)

            counter = 0
            solve_sudoku(grid_copy)
            if counter != 1:
                grid[row][column] = deleted_number
                attempts -= 1


grid = create_empty_grid()
fill_grid(grid)

remove_numbers_from_grid(grid)
solve_sudoku(grid)

