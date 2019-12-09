from tree import Node
from tree import Tree
from k_tree_maximizer import KTreeMaximizer
from tree_generator import TreeGenerator
from tree_printer import PrintMyTree


root = Node(10)

sub_root_1 = Node(2)

root.children = [sub_root_1]
sub_root_1.parent = root

tree = TreeGenerator(max_height=4, max_children=3).generate_tree()
PrintMyTree(tree.root)


subtrees_to_remove = KTreeMaximizer(tree).maximize(3)

print('ANSWER: ')
for subtree in subtrees_to_remove:
    print(str(subtree), end = ' ')

tree.remove_subtrees(subtrees_to_remove)
PrintMyTree(tree.root)