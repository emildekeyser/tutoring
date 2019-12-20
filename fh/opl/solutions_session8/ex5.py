# each node in BST is represented as [left_child, value, right_child]
def bst_insert(tree, item):
    if len(tree) == 0:
        tree.append([])
        tree.append(item)
        tree.append([])
    elif len(tree) == 3:
        if item <= tree[1]:
            bst_insert(tree[0], item)
        else:
            bst_insert(tree[2], item)


def bst_search(tree, item):
    current_node = tree
    path = []
    while len(current_node) == 3:
        path.append(current_node[1])
        if current_node[1] == item:
            return current_node, path
        elif current_node[1] < item:
            current_node = current_node[2]
        else:
            current_node = current_node[0]
