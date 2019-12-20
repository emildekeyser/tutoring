#NOTE: RECURSION IS USED IN HELPER FUNCTIONS BUT ITERATIVE APPROACHES IN THESE FUNCTIONS ARE ALLOWED AS WELL
from math import sqrt, floor

# OPDRACHT 1
def clone_sudoku(sudoku):
    # check for empty sudoku
    if not sudoku:
        return []
    # return the first row of the sudoku and recursively call clone_sudoku to return the rest
    return [sudoku[0]] + clone_sudoku(sudoku[1:])


# returns the square root of a function rounded
def integer_sqrt(x):
    return floor(sqrt(x) + 0.5)

# get a block from the sudoku as a list (not as a matrix)
def get_block_as_list(sudoku, block_number):
    size = len(sudoku)
    root = integer_sqrt(size)
    # Horizontal/vertical coordinate of the upper-left square in block with block number block_number
    x = (block_number // root) * root
    y = (block_number % root) * root
    return get_block_as_list2(sudoku,size - 1,x,y,root)

# Helper function for get_block_as_list that does the heavy calculations
def get_block_as_list2(sudoku,pos_in_block,x,y,root):
    if pos_in_block < 0:
        return []
    return [sudoku[x + (pos_in_block // root)][y + (pos_in_block % root)]] + get_block_as_list2(sudoku,pos_in_block - 1,x,y,root)


# get row from sudoku as a list
def get_row_as_list(sudoku, row_number):
    return sudoku[row_number]

# get column from sudoku as a list
def get_column_as_list(sudoku, column_number):
    if not sudoku:
        return []
    return [sudoku[0][column_number]] + get_column_as_list(sudoku[1:], column_number)


# the above functions transform everything into a list and this function then checks for doubles
def check_list(list_of_numbers):
    """
    Checks if the given list contains the same truthful value twice.
    Note that "None" is not a truthful value, and numbers are.
    :param list_of_numbers: List to check.
    :return: True if the list does not contain the same truthful value twice.
    """

    def check_list2(values_to_check, values_seen):
        if not values_to_check:  # base case - an empty array
            return True
        if values_to_check[0] in values_seen:  # recursion case - this is the second time we enounter the same value
            return False
        if values_to_check[0]:  # only add truthful values to to values_seen
            values_seen.add(values_to_check[0])
        return check_list2(values_to_check[1:], values_seen)

    return check_list2(list_of_numbers, set())

# OPDRACHT 2
def maybe_valid_sudoku(sudoku):
    def maybe_valid_sudoku2(sudoku, count):
        if count < 0:
            return True
        # Note that Python evaluates boolean expressions lazily, so we will not do more checks than necessary.
        # https://docs.python.org/2/reference/expressions.html#boolean-operations
        return check_list(get_block_as_list(sudoku, count)) \
               and check_list(get_row_as_list(sudoku, count)) \
               and check_list(get_column_as_list(sudoku, count)) \
               and maybe_valid_sudoku2(sudoku, count - 1)

    return maybe_valid_sudoku2(sudoku, len(sudoku) - 1)


def size_row_col_from_pos(sudoku, pos):
    size = len(sudoku)
    return size, pos // size, pos % size


def solve_sudoku_recursive_postions(sudoku, pos):
    """
    Function that fills in the given Sudoku starting from the given position.

    :param sudoku: Sudoku to be filled in. If filling in under the given conditions is not possible,
        Sudoku is the same after completion of this function as before this function was called.
    :returns True iff filling in sudoku from the given position is possible and the (possibly partially filled)

    Postcondition: If possible, sudoku conforms to the Sudoku rules; only None values have changed.
    """
    size, row, col = size_row_col_from_pos(sudoku, pos)
    # If the sudoku does not conform to the sudoku rules, stop with unsuccessful return status
    if not maybe_valid_sudoku(sudoku):
        return False
    # Otherwise, if no filling is required, stop with successful return status
    if pos >= size * size:
        return True
    # Otherwise, if this position is already filled, the result is identical as when calling it on the next position
    if sudoku[row][col] is not None:
        return solve_sudoku_recursive_postions(sudoku, pos + 1)
    # Otherwise, rephrase this function in terms of solve_sudoku_recursive_guesses
    return solve_sudoku_recursive_guesses(sudoku, pos, 1)


def solve_sudoku_recursive_guesses(sudoku, pos, guess):
    """
    Function that starts filling in the given Sudoku starting from the given position, under the condition that the
    element at position pos is not part of the Sudoku assignment and is greater-than-or-equal-to guess.

    :param sudoku: Sudoku to be filled in. If filling in under the given conditions is not possible,
        sudoku is the same after completion of this function as before this function was called.
    :returns True iff filling in sudoku is possible under the Sudoku rules.
    """
    size, row, col = size_row_col_from_pos(sudoku, pos)
    if guess > size:
        # Filling in under this condition is impossible - we have to restore the state of this position before backtracking
        # to an earlier position.
        sudoku[row][col] = None
        return False
    # Fill in the given lowest-possible value for the given position
    sudoku[row][col] = guess
    # If filling in the remainder of the sudoku is not successful...
    is_filling_remaining_successful = solve_sudoku_recursive_postions(sudoku, pos + 1)
    if not is_filling_remaining_successful:
        # ... then this function with the given arguments is identical as when calling it with a larger lower bound on guess.
        return solve_sudoku_recursive_guesses(sudoku, pos, guess + 1)
    else:
        # Otherwise, we have found the solution!
        return True

# OPDRACHT 3
def solve_sudoku(sudoku):
    cloned_sudoku = clone_sudoku(sudoku)
    solve_sudoku_recursive_postions(cloned_sudoku, 0)
    return cloned_sudoku






import unittest

class TestEx1(unittest.TestCase):
    def setUp(self):
        self.sudoku9_0 = [
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

        self.sudoku9_0_solution = [
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

        self.sudoku9_1 = [
            [1, None, None, None, None, None, None, None, 6],
            [None, None, 6, None, 2, None, 7, None, None],
            [7, 8, 9, 4, 5, None, 1, None, 3],
            [None, None, None, 8, None, 7, None, None, 4],
            [None, None, None, None, 3, None, None, None, None],
            [None, 9, None, None, None, 4, 2, None, 1],
            [3, 1, 2, 9, 7, None, None, 4, None],
            [None, 4, None, None, 1, 2, None, 7, 8],
            [9, None, 8, None, None, None, None, None, None]
        ]

        self.sudoku4_1 = [[1, 2, None, None],
                          [3, 4, 1, 2],
                          [2, 3, 4, 1],
                          [4, 1, 2, 3]]

        self.sudoku4_1_backup = [[1, 2, None, None],
                                 [3, 4, 1, 2],
                                 [2, 3, 4, 1],
                                 [4, 1, 2, 3]]

        self.sudoku4_1_solution = [[1, 2, 3, 4],
                                   [3, 4, 1, 2],
                                   [2, 3, 4, 1],
                                   [4, 1, 2, 3]]

    def test_get_block_as_list(self):
        self.assertEqual(get_block_as_list(self.sudoku4_1, 0), [1, 2, 3, 4][::-1])
        self.assertEqual(self.sudoku4_1, self.sudoku4_1_backup)
        self.assertEqual(get_block_as_list(self.sudoku4_1, 1), [None, None, 1, 2][::-1])
        self.assertEqual(get_block_as_list(self.sudoku4_1, 2), [2, 3, 4, 1][::-1])
        self.assertEqual(get_block_as_list(self.sudoku4_1, 3), [4, 1, 2, 3][::-1])
        self.assertEqual(get_block_as_list(self.sudoku9_1, 0), [1, None, None, None, None, 6, 7, 8, 9][::-1])
        self.assertEqual(get_block_as_list(self.sudoku9_1, 1), [None, None, None, None, 2, None, 4, 5, None][::-1])
        self.assertEqual(get_block_as_list(self.sudoku9_1, 8), [None, 4, None, None, 7, 8, None, None, None][::-1])

    def test_get_row_as_list(self):
        self.assertEqual(get_row_as_list(self.sudoku4_1, 0), [1, 2, None, None])
        self.assertEqual(get_row_as_list(self.sudoku4_1, 1), [3, 4, 1, 2])
        self.assertEqual(get_row_as_list(self.sudoku4_1, 2), [2, 3, 4, 1])
        self.assertEqual(get_row_as_list(self.sudoku4_1, 3), [4, 1, 2, 3])
        self.assertEqual(get_row_as_list(self.sudoku9_1, 2), [7, 8, 9, 4, 5, None, 1, None, 3])

    def test_get_column_as_list(self):
        self.assertEqual(get_column_as_list(self.sudoku4_1, 0), [1, 3, 2, 4])
        self.assertEqual(get_column_as_list(self.sudoku4_1, 3), [None, 2, 1, 3])
        self.assertEqual(get_column_as_list(self.sudoku9_1, 0), [1, None, 7, None, None, None, 3, None, 9])
        self.assertEqual(get_column_as_list(self.sudoku9_1, 8), [6, None, 3, 4, None, 1, None, 8, None])

    def test_check_list(self):
        self.assertFalse(check_list([5, 3, 1, 2, 7, 4, 1, 2, 1]))
        self.assertFalse(check_list([5, 3, 1, 2, 7, 4, 1, 2, None]))
        self.assertFalse(check_list([5, 1, None, None, None, None, None, None, 1]))
        self.assertTrue(check_list([None, None, 1, 2]))
        self.assertTrue(check_list([3, None, 1, None]))

    def test_check_sudoku(self):
        self.assertTrue(maybe_valid_sudoku(self.sudoku9_1))

    def test_solve_sudoku(self):
        self.assertEqual(solve_sudoku(self.sudoku4_1), self.sudoku4_1_solution)
        self.assertEqual(solve_sudoku(self.sudoku9_0), self.sudoku9_0_solution)


if __name__ == '__main__':
    print("Hello world!")
    unittest.main()