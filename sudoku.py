# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 0],
# ]

# board = [
#     [1, 0, 0, 0, 0, 0, 0, 8, 0],
#     [0, 7, 0, 0, 9, 0, 3, 4, 0],
#     [0, 0, 9, 0, 0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 3, 0, 0, 0, 8],
#     [4, 0, 0, 0, 0, 5, 6, 3, 0],
#     [0, 6, 0, 0, 0, 0, 0, 0, 2],
#     [0, 0, 0, 0, 0, 0, 0, 0, 6],
#     [0, 4, 0, 0, 2, 0, 7, 9, 0],
#     [5, 0, 0, 1, 0, 0, 0, 0, 0],
# ]
board = [
    [1,0,0,0,0,7,0,9,0],
    [0,3,0,0,2,0,0,0,8],
    [0,0,9,6,0,0,5,0,0],
    [0,0,5,3,0,0,9,0,0],
    [0,1,0,0,8,0,0,0,2],
    [6,0,0,0,0,4,0,0,0],
    [3,0,0,0,0,0,0,1,0],
    [0,4,0,0,0,0,0,0,7],
    [0,0,7,0,0,0,3,0,0]
]

# show the grid in a stylish
def show_grid(bo):
    for i in range(len(bo)):
        print(bo[i])
    print("\n -------- Résolu -------- !")

# check if case is empty
def is_empty(bo, x, y):
    if(bo[x][y] == 0):
        return True
    return False

# check if number is already in line 
def not_number_in_line(number, x, bo):
    for i in range(len(bo[0])):
        if(bo[x][i] == number):
            return False
    return True

# check if number is already in column 
def not_number_in_column(number, y, bo):
    for i in range(len(bo)):
        if(bo[i][y] == number):
            return False
    return True
    
# check if number is already in the square
def not_number_is_square(number, x, y, bo):
    x_base = (x // 3) * 3
    y_base = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if bo[x_base + i][y_base + j] == number:
                return False
    return True


# check if number is valid
def is_valid(number, x, y, bo):
    if(not_number_in_line(number, x, bo) and not_number_in_column(number, y, bo) and not_number_is_square(number, x, y, bo)):
        return True
    return False

# solve the board
def solve_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(is_empty(bo, i, j)):
                for k in range(1, 10):
                    if(is_valid(k, i, j, bo)):
                        bo[i][j] = k
                        solve_board(bo)
                    bo[i][j] = 0
                return
    show_grid(bo)    
solve_board(board)