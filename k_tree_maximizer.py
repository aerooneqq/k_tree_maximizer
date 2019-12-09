class DpCell:

    def __init__(self, value, parent_index):

        self.value = value
        self.parent_index = parent_index


    def __str__(self):
        return '{' + str(self.value) + ',' + str(self.parent_index) + '}'


class KTreeMaximizer:

    def __init__(self, tree):

        self.tree = tree
        self.nodes_collection = tree.get_nodes_array()
        self.child_parent_map = tree.get_child_parent_map()
        self.nodes_count = tree.size
        self.dp = []
    

    def _init_dp(self, max_iter_count):

        for _ in range(max_iter_count + 1):
            self.dp.append([DpCell(-1000, -1) for _ in range(self.nodes_count)])


    def _check_if_parent_deleted(self, row, curr_col, prev_col) -> bool:
        
        node = self.nodes_collection[curr_col]

        while (row > 0 and prev_col > -1):
            prev_node = self.nodes_collection[prev_col]

            if (prev_node in self.child_parent_map.get(node)):
                return True
            
            row -= 1
            prev_col = self.dp[row + 1][prev_col].parent_index

        return False


    def _check_if_node_in_path(self, node_index, row, col) -> bool:
        
        while (row > 0 and col > -1):
            if (node_index == col):
                return True
            
            col = self.dp[row][col].parent_index
            row -= 1

        return False


    @staticmethod
    def _check_if_any_in_set(nodes, parents) -> bool:

        for node in parents:
            if (node in nodes):
                return True

        return False


    def _check_if_any_parent_in_array(self, array, node):
        nodes_to_delete = []
        for el in array:
            if (node in el.get_all_parents()):
                nodes_to_delete.append(el)

            if (el in node.get_all_parents()):
                return (True, [])

        return (False, nodes_to_delete)


    def _calculate_profit(self, start_node, row, col) -> int:

        nodes = [start_node]

        while (row > 0 and col > -1):
            curr_node = self.nodes_collection[col] 
            res, nodes_to_delete = self._check_if_any_parent_in_array(nodes, curr_node)
            
            if (not res and curr_node not in nodes):
                for node_to_del in nodes_to_delete:
                    nodes.remove(node_to_del)

                nodes.append(curr_node)

            row -= 1
            col = self.dp[row + 1][col].parent_index

        profit = 0
        for node in nodes: 
            profit += node.subtree_weight

        return -profit


    def maximize(self, max_iter_count):

        self.tree.calculate_subtree_weights_rec(self.tree.root)
        self._init_dp(max_iter_count)

        for index, cell in enumerate(self.dp[1]):
            cell.value = -self.nodes_collection[index].subtree_weight

        for i in range(2, max_iter_count + 1):
            for j in range(self.nodes_count):
                for k in range(self.nodes_count):

                    if (j != k):
                        if (self._check_if_node_in_path(j, i - 1, k)):

                            if (self.dp[i - 1][k].value > self.dp[i][j].value):
                                self.dp[i][j] = DpCell(self.dp[i - 1][k].value, self.dp[i - 1][k].parent_index)
                        
                        elif (not self._check_if_parent_deleted(i, j, k)):

                            curr_node = self.nodes_collection[j]
                            profit = self._calculate_profit(curr_node, i - 1, k)

                            if (profit > self.dp[i][j].value):
                                self.dp[i][j].value = profit
                                self.dp[i][j].parent_index = k

        #self._print_dp()

        return self.get_answer()


    def get_answer(self):

        max_row = 0
        max_col = 0

        for row_index, row in enumerate(self.dp): 
            for col_index, cell in enumerate(row):
                if (cell.value > self.dp[max_row][max_col].value):
                    max_row = row_index
                    max_col = col_index

        answer = []

        if (self.dp[max_row][max_col].value <= 0):
            return answer

        while (max_row > 0 and max_col > -1):
            answer.append(self.nodes_collection[max_col])

            max_col = self.dp[max_row][max_col].parent_index
            max_row -= 1

        return answer


    def _print_dp(self):

        for row in self.dp:
            for cell in row:
                print(str(cell), end = '\t')

            print()