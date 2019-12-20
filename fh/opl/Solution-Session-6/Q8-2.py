'''
Directed graph
'''

def add_to_graph(graph, x, y=None):
    if y is not None:
        if x in graph.keys():
            successors = graph[x]
            successors.add(y)
            graph[x] = successors
        else:
            graph[x] = {y}

        if y not in graph.keys():
            graph[y] = set()
    else:
        if x not in graph.keys():
            graph[x] = set()

def input_graph():
    graph = {}
    input_string = input("Input an edge (Node1 Node2) or a node (Node1): ")
    while input_string != "QQQ":
        temps = input_string.split()
        if len(temps) == 2:

            x, y = int(temps[0]), int(temps[1])

            add_to_graph(graph, x, y)

        if len(temps) == 1:
            x = int(temps[0])
            add_to_graph(graph, x)

        input_string = input("Input an edge (Node1 Node2) or a node (Node1): ")
    return graph

def is_isolated(graph, nd):
    if len(graph[nd]) != 0:
        return False

    for k in graph.keys():
        if k != nd:
            if nd in graph[k]:
                return False

    return True

def connected_to_common(graph, nd1, nd2):

    sub1 = graph[nd1]
    sub2 = graph[nd2]
    if len(sub1.intersection(sub2)) > 0:
        return True

    return False

def has_loop(graph):
    for nd in graph.keys():
        if nd in graph[nd]:
            return True
    return False

def has_path(graph, nd1, nd2):
    lst = list(graph[nd1])
    idx = 0
    while idx < len(lst):
        for t in graph[lst[idx]]:
            if t not in lst:
                lst.append(t)
        idx += 1
    if nd2 in lst:
        return True
    return False



def test():

    g = input_graph()
    print(g)
    print(is_isolated(g, 2))
    print(has_loop(g))
    print(connected_to_common(g, 0, 3))
    print(connected_to_common(g, 1, 3))
    print(has_path(g, 1, 4))


test()
