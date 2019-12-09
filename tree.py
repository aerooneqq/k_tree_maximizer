class Node:

    def __init__(self, value: int):

        self.value = value
        self.children = []
        self.parent = None
        self.subtree_weight = 0

    
    def check_if_deep_parent(self, parent):

        curr_parent = self.parent

        while not curr_parent is None:
            if (curr_parent == parent):
                return True
            
            curr_parent = curr_parent.parent

        return False


    def get_all_parents(self):

        parents = set()
        parent = self.parent

        while (parent is not None):
            parents.add(parent)
            parent = parent.parent

        return parents

    
    def __str__(self):
        return str(self.value)


class Tree:

    def __init__(self, root):
        self.root = root
        self.size = self._count_nodes()


    def _count_nodes(self) -> int:

        if (self.root is None): return

        size = 0
        pending_nodes = [self.root]

        while len(pending_nodes) > 0:
            size += 1
            curr_node = pending_nodes.pop()
            pending_nodes.extend(curr_node.children)

        return size


    def get_nodes_array(self):

        if (self.root is None): return []

        nodes = []

        pending_nodes = [self.root]

        while len(pending_nodes) > 0:
            curr_node = pending_nodes.pop()
            nodes.append(curr_node)
            pending_nodes.extend(curr_node.children)

        return nodes


    def get_child_parent_map(self):

        child_parent_map = dict()

        pending_nodes = [self.root]
        
        while (len(pending_nodes) > 0):
            curr_node = pending_nodes.pop()

            child_parent_map[curr_node] = curr_node.get_all_parents()

            pending_nodes.extend(curr_node.children)

        return child_parent_map


    def calculate_subtree_weights_rec(self, node):

        if (len(node.children) == 0):
            node.subtree_weight = node.value
            return

        for child in node.children:
             self.calculate_subtree_weights_rec(child)

        weight = node.value

        for child in node.children:
            weight += child.subtree_weight
        
        node.subtree_weight = weight


    def remove_subtrees(self, subtrees_roots):

        if self.root in subtrees_roots:
            self.root = Node(0)
            return

        pending_nodes = [self.root]

        while (len(pending_nodes) > 0):
            
            node = pending_nodes.pop()

            for subtree_root in subtrees_roots:
                if (subtree_root in node.children):
                    node.children.remove(subtree_root)

            pending_nodes.extend(node.children)
