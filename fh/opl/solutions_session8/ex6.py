from ex5 import bst_insert


def bst_build(random_list):
    bst = []
    for item in random_list:
        bst_insert(bst, item)
    return bst


def bst_tolist(bs_tree):
    ret = []
    if len(bs_tree) == 3:

        # extend            vs      append
        # >>> a = [1,2,3]           >>> a = [1,2,3]
        # >>> a.extend([4])         >>> a.append([4])
        # >>> a                     >>> a
        # [1,2,3,4]                 [1,2,3,[4]]

        ret.extend(bst_tolist(bs_tree[0]))
        ret.append(bs_tree[1])
        ret.extend(bst_tolist(bs_tree[2]))
    return ret


def bst_sort(random_list):
    return bst_tolist(bst_build(random_list))

