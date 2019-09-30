# Complexity
N = number of nodes in tree
U = number of users per node
n = N * U

Time - O(n)
Space - O(n)

# Explanation
Fairly straightforward. We are interested in whether a user is in a group where a group can contain a list of users or a list of other groups. This means that in order for us to determine whether a group contains a user, we have to consider all of its child groups.

Recursion is the key here, we call the same method that determines the presence of a user in a group, then call that same function on each of the group's children until we have considered everything down to the leaf nodes stemming from our original node.

Tree traversal requires us to visit every node in the tree (worst case). We are also performing a search for a user at each node we visit. Note: if this collection of users was a Set or another data structure that supported O(1) lookups, each node could support an unlimited number of users without impacting the performance of this search.

As it currently stands, if we assume that there is an even distribution of users between groups, then adding more nodes to the tree will result in a linear increase in the time required for this algorithm - hence the time & space complexity of O(n)
