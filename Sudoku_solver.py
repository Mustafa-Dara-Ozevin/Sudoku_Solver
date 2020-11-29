sudoku = [
    [0,0,7,0,0,3,9,0,2],
    [0,0,0,8,0,0,0,0,0],
    [9,4,3,0,0,0,0,0,7],
    [6,9,0,0,0,0,0,0,0],
    [3,0,0,5,2,7,0,0,0],
    [0,0,0,0,0,0,8,4,0],
    [0,0,0,0,4,8,0,0,0],
    [2,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,2,9]
]

def format(sudoku):
    sudoku_formatted = sudoku
    for row in range(len(sudoku_formatted)):
        for i in [3,7]:
             sudoku_formatted[row].insert(i,'|')

        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - - - - - - - ')
        print(sudoku_formatted[row])
        
    

def find_empty_square(sudoku):
    for row in range(len(sudoku)):
        for column in range(len(sudoku[row])):
            if sudoku[row][column] == 0:
                return row,column
            



def check_square(number,row_index,column_index,sudoku):
    checked_number = number
    #check on row
    for number in sudoku[row_index]:
        if number == checked_number:
            return False
    
    #check on column
    for row in sudoku:
        if row[column_index] == checked_number:
            return False
    
    #check on square
    square_row = round(row_index/3-0.3)
    square_column = round(column_index/3-0.3)
    for row in range(square_row*3,square_row*3+3):
        for column in range(square_column*3,square_column*3+3):
            if sudoku[row][column] == checked_number:
                return False
    return True

def solve_sudoku(sudoku):
    find = find_empty_square(sudoku)
    if not find:
        return True
    row_index,column_index = find
    for i in range(1,10):      
        if check_square(i,row_index,column_index,sudoku):
            sudoku[row_index][column_index] = i

            if solve_sudoku(sudoku):
                return True

            sudoku[row_index][column_index] = 0

    return False


solve_sudoku(sudoku)
format(sudoku)