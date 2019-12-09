This is the projcet where i test the "greedy dynamic programming" approach to solve the problem of maximization the tree no more than in K steps.

In order to solve the problem of maximization tree in no more than K steps we create a
DP matrix [maxOperationsCount + 1, nodesCount]. Each column corresponds to the node from nodeCollection
(if we have a column with index J then it corresponds to the node_collection[J] node).
Each row is a i-th iteration.
The first row contains only zeroes.
The second row contains the subtree weights of every node.

The idea of this DP is that every cell in the DP matrix is a maximum profit we can get after deletion of the
node which corresponds to this cell on the i-th iteration (i = cell's row index). To calculate this profit we monitor
the i - 1 row, and see what happens if we delete the current node, assuming the fact the we deleted the k-th node from the
i - 1 row. Each DP cell has a parentIndex field which tells us from where from the previous row we got the maximum profit.
So when we monitor k-th cell from the previous row we check, have we already deleted any parent of the current node. If so,
we don't look at this case. If there was no deletion of a parent of the current node, then we calculate the profit. We must
be very careful here, because in any previous step we could have deleted the child of the current node, so it's profit will not
be just the subtree weight of the current node. We have to look at the deletion history, and if we have deleted the
child of this node, we must count it. After that, if the profit is greater than
the value in this DP cell, we update it, and also update the parent index of the current cell.