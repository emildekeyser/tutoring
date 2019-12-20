'''
Undirected graph
'''

def add_to_graph(graph, x, y=None):
    '''
    add to graph
    :param graph:
    :param x: a node
    :param y: the second node (optional)
    :return: None
    '''
    if y is not None:
        if x in graph:
            #add y to the successors of x
            graph[x].add(y)
        else:
            graph[x] = {y}

        if y in graph:
            #add x to the successors of y
            graph[y].add(x)
        else:
            graph[y] = {x}
    else:
        if x not in graph:
            # if no y is supplied simply add x with no successors
            graph[x] = set()




def input_graph():
    graph = {}
    input_string = input("Input an edge (Node1 Node2) or a node (Node1): ")
    while input_string != "QQQ":
        temps = input_string.split()
        if len(temps) == 2:  # if input is an edge

            x, y = int(temps[0]), int(temps[1])

            add_to_graph(graph, x, y)

        if len(temps) == 1:
            x = int(temps[0])
            add_to_graph(graph, x)  # if input is a node

        input_string = input("Input an edge (Node1 Node2) or a node (Node1): ")
    return graph

def is_isolated(graph, nd):
    '''
    check if nd is isolated in graph
    :param graph:
    :param nd:
    :return:
    '''
    return len(graph[nd]) == 0


def connected_to_common(graph, nd1, nd2):
    '''
    check if two nodes nd1 and nd2 are connected to a common node
    :param graph:
    :param nd1:
    :param nd2:
    :return:
    '''
    successors1 = graph[nd1]
    successors2 = graph[nd2]
    return len(successors1.intersection(successors2))>0

def has_loop(graph):
    for nd in graph.keys():
        if nd in graph[nd]:
            return True
    return False

def has_path(graph, nd1, nd2):
    #list with all nodes that are reachable from nd1
    lst = list(graph[nd1])
    idx = 0
    while idx < len(lst):
        # list[idx] is a node reachable from nd1
        # loop over all successors of list[idx]
        for t in graph[lst[idx]]:
            # all successors of list[idx] are also reachable from nd1
            # add them to the list of reachable nodes if they are not already in there
            if t not in lst:
                lst.append(t)
        #investigate next node
        idx += 1
    if nd2 in lst:
        return True
    return False



def test():
    g = input_graph()
    print(g)
    print(is_isolated(g, 2))
    print(has_loop(g))
    print(connected_to_common(g, 1, 4))
    print(connected_to_common(g, 1, 3))
    print(has_path(g, 0, 3))

test()
