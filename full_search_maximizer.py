from tree import Tree
from tree import Node


class FullSearchMaximizer:

    def __init__(self, tree):
        self.tree = tree
        self.nodes_collection = tree.get_nodes_array()
        self.child_parent_map = tree.get_child_parent_map()
        self.nodes_count = tree.size