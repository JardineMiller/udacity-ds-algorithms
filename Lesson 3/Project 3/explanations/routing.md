# Complexity

## Add Handler:
* Time: O(l)
* Space: O(n)

## Lookup:
* Time: O(l)
* Space: O(n)

# Explanation
## Add Handler:
Time: As we need to start from the root node in order to add a new handler, it is reasonable to assume that, in the worst case, we have to iterate over each level of the tree. Therefore, our time complexity is linear and will increase as the number of levels in the Trie increases, so O(l) where l is equal the maximum number of levels in the tree.

Space: In order to iterate over the tree to find the correct point to add our handler node, we need to store the entire tree in memory. Therefore our space complexity here is O(n) where n equals the total number of nodes in our tree.

## Lookup:
Time: As we need to start from the root node in order to find a leaf node, it is reasonable to assume that, in the worst case, we have to iterate over each level of the tree. Therefore, our time complexity is linear and will increase as the number of levels in the Trie increases, so O(l) where l is equal the maximum number of levels in the tree.

Space: In order to iterate over the tree to find a leaf node, we need to store the entire tree in memory. Therefore our space complexity here is O(n) where n equals the total number of nodes in our tree.