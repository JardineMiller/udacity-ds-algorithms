# Complexity

## Add Handler:
* Time: O(l)
* Space: O(n)

## Lookup:
* Time: O(l + m)
* Space: O(n + m)

# Explanation
The solution uses a Trie to store all the possible combination of paths for our Router. Whenever we add a handler, we have to split the path (O(m) where m = len of path) we uses a simple iterator to traverse all the nodes until we find the suitable leaf node (O(l) where l = num of levels). In order to handle trailing slashes (and the index slash), we simply continue to the next iteration of the loop within RouteTrie.find().

## Add Handler:
Time: As we need to start from the root node in order to add a new handler, it is reasonable to assume that, in the worst case, we have to iterate over each level of the tree (or each sub-path in the path). In order to split the path, we need to iterate over the entire path and split it based on a certain character. Therefore, our time complexity is linear and will increase as the number of levels in the Trie increases, so O(l + m) where l is equal the maximum number of levels in the tree and m is equal to the number of sub-paths are in the overall path.

Space: In order to iterate over the tree to find the correct point to add our handler node, we need to store the entire tree in memory. Therefore our space complexity here is O(n) where n equals the total number of nodes in our tree.

## Lookup:
Time: As we need to start from the root node in order to find a leaf node, it is reasonable to assume that, in the worst case, we have to iterate over each level of the tree (or each sub-path in the path). Therefore, our time complexity is linear and will increase as the number of levels in the Trie increases, so O(l) where l is equal the maximum number of levels in the tree and m is equal to the number of sub-paths are in the overall path.

Space: In order to iterate over the tree to find a leaf node, we need to store the entire tree in memory. Therefore our space complexity here is O(n) where n equals the total number of nodes in our tree.