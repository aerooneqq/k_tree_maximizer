import print_tree.print_tree


class PrintMyTree(print_tree.print_tree):

    def get_children(self, node):
        return node.children


    def get_node_str(self, node):
        return '[' + str(node) + ']'
