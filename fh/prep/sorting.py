import random

# EX1
def list_generator(start, end, length, want_sorted=False):
    r = [random.randint(start, end) for _ in range(length)]
    if want_sorted:
        return sorted(r)
    else:
        return r

# EX2
def is_sorted(l):
    if len(l) < 2: return True
    a, b = l[0], l[1]
    if a > b: return False
    return is_sorted(l[1:])

def shotgun_sort(l):
    while not is_sorted(l):
        random.shuffle(l)
        print(l)
    return l

# EX3
def bubblesort(lst):
    for x in range(len(lst)):
        for i in range(len(lst) - x - 1):
            a, b = lst[i], lst[i + 1]
            if a > b:
                lst[i] = b
                lst[i + 1] = a
    return lst

# EX4
def binary_search(l, value):
    index = len(l) // 2
    a = 0
    b = len(l)
    while l[index] != value and index > 0 and index < len(l) - 1:
        if l[index] > value:
            b = index
            index = a + ((b - a) // 2)
        else:
            a = index
            index = a + ((b - a) // 2)
        print(a, index, b)
    if l[index] != value: return None
    return index

# EX 5
def insert(bst, item):
    if bst == (): return (item, (), ())
    val, left, right = bst
    if item <= val: return (val, insert(left, item), right)
    return (val, left, insert(right, item))

def search(bst, item):
    return search_path(bst, item, "")

def search_path(bst, item, path):
    if bst == (): return path
    val, left, right = bst
    # if left == () and item <= val: return path
    # if right == () and item > val: return path
    path += "/" + str(val)
    if item == val: return path
    if item < val: return search_path(left, item, path)
    return search_path(right, item, path)

# EX 6
def build_tree(lst):
    bst = ()
    for x in lst:
        bst = insert(bst, x)
    return bst

def build_list(bst):
    if bst == (): return []
    val, left, right = bst
    return build_list(left) + [val] + build_list(right)

# import unittest
# class TestEx1(unittest.TestCase):
    # def setUp(self):
    #     self.sudoku4_1_solution = [[1, 2, 3, 4],
    # def test_get_column_as_list(self):
    #     self.assertEqual(get_column_as_list(self.sudoku4_1, 0), [1, 3, 2, 4])
    # def test_check_list(self):
    #     self.assertFalse(check_list([5, 3, 1, 2, 7, 4, 1, 2, 1]))
    #     self.assertTrue(check_list([3, None, 1, None]))

    # def test_list_generator(self):
    #     l = list_generator(10, 20, 50)
    #     print(l)
    #     self.assertEqual(len(l), 50)
    #     l = list_generator(10, 20, 50, True)
    #     print(l)
    #     self.assertTrue(l[0] <= l[1])

if __name__ == '__main__':
    # unittest.main()
    # bst = build_tree([5, 1, 2, 7, 9, 14, 5])
    # print(build_list(bst))
    # for x in [5, 1, 2, 7, 9, 14]:
    #     print(search(bst, x))

    lst = list_generator(0, 10, 10)
    print(lst)
    print(bubblesort(lst))


