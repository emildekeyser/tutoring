#NOTE: RECURSION IS USED IN HELPER FUNCTIONS BUT ITERATIVE APPROACHES IN THESE FUNCTIONS ARE ALLOWED AS WELL
from math import sqrt, floor

def integer_sqrt(x):
    return floor(sqrt(x) + 0.5)


def get_blk_number_from_pos(sudoku, pos):
    row, col = pos
    root = integer_sqrt(len(sudoku))
    blk_col = col // root
    blk_row = row // root
    return blk_col + blk_row * root


def get_blk_positions(sudoku, blk_number):
    size = len(sudoku)
    root = integer_sqrt(size)
    # Horizontal / vertical coordinate of the upper-left square in block with block number block_number
    x = (blk_number // root) * root
    y = (blk_number % root) * root
    return set([(x + counter // root, y + counter % root) for counter in range(size)])


def get_row_positions(sudoku, row_number):
    size = len(sudoku)
    return set([(row_number, col_number) for col_number in range(size)])


def get_col_positions(sudoku, col_number):
    size = len(sudoku)
    return set([(row_number, col_number) for row_number in range(size)])


def get_related_positions(sudoku, pos):
    row_number, col_number = pos
    related = get_row_positions(sudoku, row_number) \
        .union(get_col_positions(sudoku, col_number)) \
        .union(get_blk_positions(sudoku, get_blk_number_from_pos(sudoku, pos)))
    related.remove((row_number, col_number))
    return related


def _get_values(sudoku, position_f, args):
    return set([frozenset(sudoku[row_number][col_number])
                for row_number, col_number in position_f(*args)])


def get_blk_values(sudoku, block_number):
    return _get_values(sudoku, get_blk_positions, [sudoku, block_number])


def get_row_values(sudoku, row_number):
    return _get_values(sudoku, get_row_positions, [sudoku, row_number])


def get_col_values(sudoku, column_number):
    return _get_values(sudoku, get_col_positions, [sudoku, column_number])


def check_filled_sudoku(sudoku_cf):
    size = len(sudoku_cf)
    correct = set([frozenset([i]) for i in range(1, size + 1)])
    for i in range(size):
        if get_blk_values(sudoku_cf, i) != correct \
                or get_col_values(sudoku_cf, i) != correct \
                or get_row_values(sudoku_cf, i) != correct:
            return False
    return True


def check_for_empty_candidates(sudoku_cf):
    return all([j for i in sudoku_cf for j in i])


def get_best_position(sudoku_cf, positions):
    best_cnt = len(sudoku_cf) + 1
    best_pos = None
    for row, col in positions:
        cnt = len(sudoku_cf[row][col])
        if cnt < best_cnt:
            best_cnt = cnt
            best_pos = (row, col)
    return best_pos


def guess_candidate(sudoku_cf, position_to_fill):
    # restore = set()
    row_number, col_number = position_to_fill
    candidates_at_position = sudoku_cf[row_number][col_number]
    guessed_candidate = candidates_at_position.pop()  # this removes the candidate; we never add the candidate back again!
    sudoku_cf[row_number][col_number] = set([guessed_candidate])
    modified_positions = set()
    for related_position in get_related_positions(sudoku_cf, position_to_fill):
        related_row_number, related_column_number = related_position
        related_candidates = sudoku_cf[related_row_number][related_column_number]
        if guessed_candidate in related_candidates:
            related_candidates.remove(guessed_candidate)
            modified_positions.add(related_position)

    def rollback_guess():
        sudoku_cf[position_to_fill] = candidates_at_position
        for modified_row_number, modified_column_number in modified_positions:
            sudoku_cf[modified_row_number][modified_column_number].add(guessed_candidate)

    return rollback_guess, modified_positions


def optimize_hidden_singles(sudoku_cf, modified_positions):
    if not modified_positions:
        return

    # Returns a list of values that can only be put at the given position
    def get_hidden_single_values(row_number, col_number):
        candidates = set(sudoku_cf[row_number][col_number])
        related_positions = get_related_positions(sudoku_cf, (row_number, col_number))
        for related_row_number, related_col_number in related_positions:
            candidates -= sudoku_cf[related_row_number][related_col_number]
        return candidates

    restore = set()
    modified = set()
    for row_number, col_number in modified_positions:
        hidden_single_values = get_hidden_single_values(row_number, col_number)
        # There are multiple values that can only be put at this position, the Sudoko cannot be solved
        if len(hidden_single_values) > 1:
            restore.add(((row_number, col_number), frozenset(sudoku_cf[row_number][col_number])))
            sudoku_cf[row_number][col_number] = []
            break  # <= minor optimization - when we know the Sudoku is not solvable, we can stop looking for more hidden singles
        # If there is a single such value, we need to fill in that value
        if len(hidden_single_values) == 1:
            restore.add(((row_number, col_number), frozenset(sudoku_cf[row_number][col_number])))
            sudoku_cf[row_number][col_number] = hidden_single_values

    def rollback():
        for pos, candidates in restore:
            sudoku_cf[pos[0]][pos[1]] = set(candidates)

    return rollback, modified


def solve_sudoku_recursive(sudoku_cf, remaining_positions):
    if not check_for_empty_candidates(sudoku_cf):
        return False
    if not remaining_positions:
        return True

    position_to_fill = get_best_position(sudoku_cf, remaining_positions)
    remaining_positions.remove(position_to_fill)
    rollback_filling_in, impacted_positions = guess_candidate(sudoku_cf, position_to_fill)
    impacted_positions = impacted_positions.union([position_to_fill])
    rollback_hidden_singles, _ = optimize_hidden_singles(sudoku_cf, impacted_positions)

    can_fill_remaining = solve_sudoku_recursive(sudoku_cf, set(remaining_positions))
    if can_fill_remaining:
        return True
    else:
        rollback_hidden_singles()
        rollback_filling_in()
        remaining_positions.add(position_to_fill)
        # Note that we are adding the position to fill back to the list of remaining positions, but that we are *not*
        # restoring the chosen candidate value to the position. The recursion is finite / ending because we are
        # removing at least one candidate value every iteration (and there are only a finite number of candidate values)
        return solve_sudoku_recursive(sudoku_cf, remaining_positions)


def all_positions(sudoku):
    size = len(sudoku)
    return set([(i, j)
                for i in range(size)
                for j in range(size)])


def get_filled_positions(sudoku):
    return set([(row, col)
                for row, col in all_positions(sudoku)
                if sudoku[row][col]])


def convert_to_candidate_form(sudoku):
    def to_candidate_form(sudoku):
        sudoku_cf = []
        for row in sudoku:
            new_row = []
            for field in row:
                if field:
                    new_row.append(set([field]))
                else:
                    new_row.append(set(range(1, size + 1)))
            sudoku_cf.append(new_row)
        return sudoku_cf

    def propagate_naked_singles(sudoku_cf, filled_positions):
        for pos in filled_positions:
            if check_for_empty_candidates(sudoku_cf):
                guess_candidate(sudoku_cf, pos)

    filled_positions = get_filled_positions(sudoku)
    size = len(sudoku)
    sudoku_cf = to_candidate_form(sudoku)
    propagate_naked_singles(sudoku_cf, filled_positions)

    return sudoku_cf


def convert_from_candidate_form(sudoku_cf):
    new_sudoku = []
    for row in sudoku_cf:
        new_row = []
        for field in row:
            if not len(field) == 1:
                # Multiple possible values remain - cannot convert from candidate form
                return None
            new_row.append(list(field)[0])
        new_sudoku.append(new_row)
    return new_sudoku


def solve_sudoku(sudoku):
    sudoku_cf = convert_to_candidate_form(sudoku)
    success = solve_sudoku_recursive(sudoku_cf, all_positions(sudoku_cf))
    if success:
        return convert_from_candidate_form(sudoku_cf)
    else:
        return None


# Important to note that PYTHON PASSES LISTS BY ASSIGNMENT

import unittest
import copy


class TestEx1(unittest.TestCase):
    def setUp(self):
        self.sudoku4_0 = [[1, 2, None, None],
                          [3, 4, 1, 2],
                          [2, 3, 4, 1],
                          [4, 1, 2, 3]]
        self.sudoku4_0_solution = [[1, 2, 3, 4],
                                   [3, 4, 1, 2],
                                   [2, 3, 4, 1],
                                   [4, 1, 2, 3]]

        self.sudoku4_0_backup = [[1, 2, None, None],
                                 [3, 4, 1, 2],
                                 [2, 3, 4, 1],
                                 [4, 1, 2, 3]]

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
        self.sudoku9_0_invalid = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 9, 4, 2, 3],
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
        self.sudoku9_1_solution = [
            [1, 2, 3, 7, 8, 9, 4, 5, 6],
            [4, 5, 6, 1, 2, 3, 7, 8, 9],
            [7, 8, 9, 4, 5, 6, 1, 2, 3],
            [2, 3, 1, 8, 9, 7, 5, 6, 4],
            [5, 6, 4, 2, 3, 1, 8, 9, 7],
            [8, 9, 7, 5, 6, 4, 2, 3, 1],
            [3, 1, 2, 9, 7, 8, 6, 4, 5],
            [6, 4, 5, 3, 1, 2, 9, 7, 8],
            [9, 7, 8, 6, 4, 5, 3, 1, 2]
        ]
        self.sudoku9_2 = [
            [1, 2, 3, 7, 8, 9, 4, 5, 6],
            [4, 5, 6, 1, 2, 3, 7, 8, 9],
            [7, 8, 9, 4, 5, 6, 1, 2, 3],
            [2, 3, 1, 8, 9, 7, 5, 6, 4],
            [5, 6, 4, 2, 3, 1, 8, 9, 7],
            [8, 9, 7, 5, 6, 4, 2, 3, 1],
            [3, 1, 2, 9, 7, 8, 6, 4, 1],
            [6, 4, 5, 3, 1, 2, 9, 7, None],
            [9, 7, 8, 6, 4, 5, 3, 1, 2]
        ]
        self.sudoku9_2_solution = None

        self.sudokus = [
            (self.sudoku4_0, self.sudoku4_0_solution),
            (self.sudoku9_0, self.sudoku9_0_solution),
            (self.sudoku9_1, self.sudoku9_1_solution),
            (self.sudoku9_2, self.sudoku9_2_solution)]

    def test_solve_sudoku(self):
        for sudoku, solution in self.sudokus:
            sudoku_copy = copy.deepcopy(sudoku)
            self.assertEqual(solve_sudoku(sudoku), solution)
            self.assertEqual(sudoku, sudoku_copy)


if __name__ == '__main__':
    print("Hello world!")
    unittest.main()