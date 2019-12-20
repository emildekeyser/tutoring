import math


def binary_search(sorted_list, needle):
    index_min = 0
    index_max = len(sorted_list) - 1
    while index_min < index_max:

        index_mid = int(math.floor((index_max + index_min) / 2.0))
        print(index_mid)
        if needle <= sorted_list[index_mid]:
            index_max = index_mid
        else:
            index_min = index_mid + 1
    if needle == sorted_list[index_max]:
        return index_max
    else:
        return None
