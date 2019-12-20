#E9 a
def count_paths(x, y):
    if x == 0 or y == 0:
        return 1
    return count_paths(x - 1, y) + count_paths(x, y - 1)

#E9 b
def find_paths(x,y):
    if y == 0 and x == 0:
        return [[(0, 0)]]

    paths = []
    if y > 0:
        paths += find_paths(x, y - 1)
    if x > 0:
        paths += find_paths(x - 1, y)
    for path in paths:
        path.insert(0, (x, y))
    return paths

def main():
    x = int(input("Please enter a x: "))
    y = int(input("Please enter a y: "))
    print("The total paths are: ", count_paths(x, y))
    print("The paths are the following: \n", find_paths(x, y))

main()
