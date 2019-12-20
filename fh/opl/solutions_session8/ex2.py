import random


def shuffle_list(given_list):
    ret = list(given_list)
    random.shuffle(ret)
    return ret


def is_sorted(given_list):
    if len(given_list) == 0:
        return True

    previous_element = given_list[0]
    for element in given_list[1:len(given_list)]:
        if element < previous_element:
            return False
        previous_element = element

    return True


def shotgun_sort(input_list):
    while not is_sorted(input_list):
        input_list = shuffle_list(input_list)
    return input_list
