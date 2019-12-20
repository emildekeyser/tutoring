import timeit
# If you can't install matplotlib, remove the line below. (plotting won't work)
import matplotlib.pyplot as plt


def insertion_sort(random_list):
    for i in range(1, len(random_list)):
        k = i
        while k > 0 and random_list[k - 1] > random_list[k]:
            x = random_list[k - 1]
            random_list[k - 1] = random_list[k]
            random_list[k] = x
            k -= 1
    return random_list


# ==> n²

def timeit_timer(size=4000):
    python_sort_timeit = timeit.Timer(stmt="list.sort(r)",
                                      setup="from ex1 import random_list; r = random_list(" + str(size) + ",0," + str(
                                          size) + ")")
    python_times = python_sort_timeit.repeat(15, 1)
    python_mean = sum(python_times) / len(python_times)
    print("Python mean: " + str(python_mean))
    bst_sort_timeit = timeit.Timer(stmt="bst_sort(r)",
                                   setup="from ex1 import random_list; from ex6 import bst_sort; r = random_list(" + str(
                                       size) + ",0," + str(size) + ")")
    bst_times = bst_sort_timeit.repeat(15, 1)
    bst_mean = sum(bst_times) / len(bst_times)
    print("BST mean: " + str(bst_mean))
    insertion_sort_timeit = timeit.Timer(stmt="insertion_sort(r)",
                                         setup="from ex1 import random_list; from ex7 import insertion_sort; r = random_list(" + str(
                                             size) + ",0," + str(size) + ")")
    insertion_times = insertion_sort_timeit.repeat(15, 1)
    insertion_mean = sum(insertion_times) / len(insertion_times)
    print("Insertion mean: " + str(insertion_mean))


def matplotlib_comparison(max_size=400):
    data = [[], [], []]
    for size in range(1, max_size):
        python_sort_timeit = timeit.Timer(stmt="list.sort(r)",
                                          setup="from ex1 import random_list; r = random_list(" + str(
                                              size) + ",0," + str(
                                              size) + ")")
        python_times = python_sort_timeit.repeat(15, 1)
        python_mean = sum(python_times) / len(python_times)
        data[0].append(python_mean)

        bst_sort_timeit = timeit.Timer(stmt="bst_sort(r)",
                                       setup="from ex1 import random_list; from ex6 import bst_sort; r = random_list(" + str(
                                           size) + ",0," + str(size) + ")")
        bst_times = bst_sort_timeit.repeat(15, 1)
        bst_mean = sum(bst_times) / len(bst_times)
        data[1].append(bst_mean)

        insertion_sort_timeit = timeit.Timer(stmt="insertion_sort(r)",
                                             setup="from ex1 import random_list; from ex7 import insertion_sort; r = random_list(" + str(
                                                 size) + ",0," + str(size) + ")")
        insertion_times = insertion_sort_timeit.repeat(15, 1)
        insertion_mean = sum(insertion_times) / len(insertion_times)
        data[2].append(insertion_mean)
    plt.plot(list(range(1, max_size)), data[0])
    plt.plot(list(range(1, max_size)), data[1])
    plt.plot(list(range(1, max_size)), data[2])
    plt.legend(["python_sort", "bst_sort", "insertion_sort"])
    plt.xlabel("List length")
    plt.ylabel("Runtime (s)")
    plt.show()


# using the conventional '__main__' here, otherwise timeit will run every called function twice due to the imports
# being in the timeit string
if __name__ == '__main__':

    # uncomment the line below to print the timeit values
    # timeit_timer()
    matplotlib_comparison()


