#E2 a
#Solution with accumulator
def maximum(list,max = 0):
    if len(list) == 0:
        return max
    if list[0] > max:
        max = list[0]
    return maximum(list[1:],max)

#Solution without accumulator
def maximum2(list):
    if len(list) == 1:
        return list[0]
    elif list[0] > list[1]:
        list.pop(1)
        return maximum2(list)
    else:
        list.pop(0)
        return maximum(list)


#E2 b
def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[-1] + sum_list(list[:-1])


def main():
    print("The max is: " + str(maximum([1,2,3,4,5,6])))
    print("The sum is: " + str(sum_list([1,2,3,4,5,6])))

main()
