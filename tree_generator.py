from tree import Tree
from tree import Node

from random import randint


class TreeGenerator:

    def __init__(self, max_height = 5, values_left_border = -10, values_right_border = 10, max_children = 5):

        self.max_height = max_height
        self.values_left_border = values_left_border
        self.values_right_border = values_right_border
        self.max_children = max_children


    def _get_random_value(self):

        return randint(self.values_left_border, self.values_right_border)


    def generate_tree(self):

        root = Node(self._get_random_value())
        curr_node = root
        curr_height = 1
        height = randint(1, self.max_height)
        pending_nodes = [curr_node]

        while (curr_height <= height):
            
            new_pending_nodes = []

            while (len(pending_nodes) > 0):

                node = pending_nodes.pop()
                children_count = randint(1, self.max_children)

                for _ in range(children_count):
                    child = Node(self._get_random_value())
                    child.parent = node
                    node.children.append(child)
                    new_pending_nodes.append(child)

            curr_height += 1
            pending_nodes = new_pending_nodes

        return Tree(root)