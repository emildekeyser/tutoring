import random


def random_list(length, start, end):
    randoms = []
    for x in range(length):
        randoms.append(random.randint(start, end))
    return randoms


def sorted_list(length, start, end):
    rlist = random_list(length, start, end)
    list.sort(rlist)
    return rlist
