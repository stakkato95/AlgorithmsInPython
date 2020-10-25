class Node(object):

    def __init__(self):
        self.values = [None, None]
        self.pointers = [None, None, None]

    def is_full(self):
        return all(x is not None for x in self.values)

    def is_empty(self):
        return all(x is None for x in self.values)

    def children_empty(self):
        return all(x is None for x in self.pointers)

    def create_children(self):
        self.pointers = [Node(), Node(), Node()]

def insert(node, parent, value):
    if value is None:
        return

    # crate children if missing
    if node.children_empty():
        node.create_children()

    # edge cases
    ##########################################################################################
    if value in node.values:
        # 'value' is already there, no duplicates are allowed
        return

    if node.values[0] is None:
        # current node is either a root or leaf
        node.values[0] = value
        return
    ##########################################################################################

    # try to insert 'value' into current node
    ##########################################################################################
    if value < node.values[0] and not node.values[1]:
        # current node is either a root or leaf AND 'value' is smaller than left value
        node.values[1] = node.values[0]
        node.values[0] = value
        return
    elif node.values[0] < value and not node.values[1]:
        node.values[1] = value
        return
    elif not all_neighbours_on_same_layer_are_full(parent) and node.is_full() and parent is not None:
        insert_to_neighbour(node, parent, value)
        return
    ##########################################################################################

    # go deeper into tree and insert to children
    ##########################################################################################
    if value < node.values[0]:
        insert(node.pointers[0], node, value)
    elif node.values[0] < value < node.values[1]:
        insert(node.pointers[1], node, value)
    else:
        insert(node.pointers[2], node, value)
    ##########################################################################################


def insert_to_neighbour(node, parent, value):
    start_node_found = False
    for child_i in range(3):
        start_node_found = start_node_found or node == parent.pointers[child_i]
        if not start_node_found:
            continue
        if node.is_empty():
            node.values[0] = value
            return
        elif value < node.values[0]:
            tmp_overflow = node.values[1]
            node.values[1] = node.values[0]
            node.values[0] = value
        elif node.values[0] < value < node.values[1]:
            tmp_overflow = node.values[1]
            node.values[1] = value
        else:
            tmp_overflow = value

        value, node = move_value_between_neighbours(child_i, tmp_overflow, parent)
        if not value:
            # all values have been moved and final value inserted where is fits
            break


def move_value_between_neighbours(child_i, tmp_overflow, parent):
    if child_i == 0:
        parent_overflow = parent.values[0]
        parent.values[0] = tmp_overflow
        return parent_overflow, parent.pointers[1]
    elif child_i == 1:
        parent_overflow = parent.values[1]
        parent.values[1] = tmp_overflow
        return parent_overflow, parent.pointers[2]
    else:
        insert(parent.pointers[child_i], parent, tmp_overflow)
        return None, None

def all_neighbours_on_same_layer_are_full(parent):
    return parent is not None and all(node.is_full() for node in parent.pointers)

def delete(value):
    pass


def height():
    pass


def min_val():
    pass


def max_val():
    pass


if __name__ == '__main__':
    root = Node()

    # fill root
    insert(root, None, 66)
    insert(root, None, 78)

    # fill left child of the root
    insert(root, None, 53)
    insert(root, None, 54)

    # cause 66 to be replaced with 55 in the root
    insert(root, None, 55)
    # add second element to the middle child
    insert(root, None, 70)

    # cause all elements to be shifted by one
    insert(root, None, 50)
    # cause all elements starting from second node to be shifted by one
    insert(root, None, 69)

    insert(root, None, 49)

    print('finished')
