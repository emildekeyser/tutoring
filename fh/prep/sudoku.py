import math

def debug(msg):
    if True: print(msg)

sudoku_fg1_start = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9, 8, None, None, None, None, 6, None],
    [8, None, None, None, 6, None, None, None, 3],
    [4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],
    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5],
    [None, None, None, None, 8, None, None, 7, 9]
]



sudoku_fg1_maybe_finish = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]

sudoku_fg1_finished = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def clone_sudoku(sudoku):
    return [row.copy() for row in sudoku]

def check_block(sudoku, x, y):
    values = []
    block_size = int(math.sqrt(len(sudoku)))
    x_block_index = ((x-1)//block_size)
    y_block_index = ((y-1)//block_size)
    for bx in range(block_size):
        for by in range(block_size):
            y_abpos = y_block_index * block_size + by
            x_abpos = x_block_index * block_size + bx
            if sudoku[y_abpos][x_abpos]:
                values.append(sudoku[y_abpos][x_abpos])
    valid = len(values) == len(set(values))
    return valid, x_block_index, y_block_index

def check_row(sudoku, y):
    numbers = [n for n in sudoku[y-1] if n]
    return len(numbers) == len(set(numbers))

def check_column(sudoku, x):
    numbers = [sudoku[y][x-1] for y in range(len(sudoku)) if sudoku[y][x-1]]
    return len(numbers) == len(set(numbers))

def maybe_valid_sudoku(sudoku):

    verified_blocks = set()
    verified_rows = set()
    verified_columns = set()

    for x in range(1, len(sudoku)+1):
        for y in range(1, len(sudoku)+1):

            if y in verified_rows or x in verified_columns: continue

            b, block_x, block_y = check_block(sudoku, x, y)

            if b and (block_x, block_y) in verified_blocks: continue

            r = check_row(sudoku, y)
            c = check_column(sudoku, x)

            if not (b and r and c): return False

            verified_blocks.add((block_x, block_y))
            verified_rows.add(y)
            verified_columns.add(x)

    return True

def solved(sudoku):
    filled = None not in [val for row in sudoku for val in row ]
    return filled and maybe_valid_sudoku(sudoku)

def get_next_pos(sudoku):
    x = y = 0
    while sudoku[y][x] != None:
        x += 1
        if x >= 9:
            x = 0
            y += 1
            if y >= 9:
                y = 8
                x = 8
                break
    return x, y

def backtrack(sudoku, x, y):
    x -= 1
    if x < 0:
        x = 8
        y -= 1
    if y < 0: y = 0
    if sudoku[y][x] == 9:
        sudoku[y][x] = None
        backtrack(sudoku, x, y)
    else:
        debug((y, x))
        sudoku[y][x] += 1

def solve_sudoku(sudoku):
    while not solved(sudoku):
        x, y = get_next_pos(sudoku)
        debug("nextpos: "+str((x, y)))
        sudoku[y][x] = 1
        while not maybe_valid_sudoku(sudoku):
            sudoku[y][x] += 1 #fill next possible value
            debug(sudoku)
            if sudoku[y][x] == 10:
                sudoku[y][x] = None
                backtrack(sudoku, x, y)
                return solve_sudoku(sudoku)
    return sudoku

def solve_sudoku2(sudoku):
    debug(sudoku)
    if solved(sudoku): return sudoku
    else:
        x, y = get_next_pos(sudoku)
        for val in range(1, 10): # get next Value
            branch = clone_sudoku(sudoku)
            branch[y][x] = val
            if maybe_valid_sudoku(branch):
                result = solve_sudoku2(branch)
                if result: return result
        return False

s = solve_sudoku2(sudoku_fg1_start)
print("-------")
print(s)
print("-------")
print(sudoku_fg1_finished)
print(sudoku_fg1_finished == s)

print(sudoku_fg1_finished == sudoku_fg1_maybe_finish)
print(solved(sudoku_fg1_maybe_finish))
