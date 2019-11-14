# Complexity

## Find:
* Time: O(l)
* Space: O(n)

## Suffixes:
* Time: O(n + m)
* Space: O(k + f)

# Explanation
For this exercise, a Trie was used to represent all the all the possible paths & relationships between letters in a series of words. A Trie is a particular useful data structure to use for this problem as it allows a O(1) lookup at each node. Even though the lookup of words within the Trie is linear - in that it increases as the number of letters in the word you're searching for - it is still much more efficient that the worse case scenario of looking up words in a list. Even though the worst case for a list search is still O(n), the size of the dataset between the two is significant. There are 171,476 words in the English dictionary in current use whilst the longest word in the English dictionary is 'pneumonoultramicroscopicsilicovolcanoconiosis' - which has 45 characters. As such, benefits of using a Trie are obvious.

## Find:
Time: As we need to start from the root node in order to find a node, it is reasonable to assume that, in the worst case, we have to iterate over each letter in the word that is being sought (as well as each level of the tree). Therefore, our time complexity is linear and will increase as the number of levels in the Trie increases, so O(l) where l is equal the maximum number of levels in the tree.

Space: In order to iterate over the tree to find the node in question, we need to store the entire tree in memory. Therefore our space complexity here is O(n) where n equals the total number of nodes in our tree.

## Suffixes:
Time: In order to find all the suitable suffixes from our current node, we have to recursively iterate over each child (and all its subsequent children etc). We are performing a depth first search here meaning our total time complexity is O(n + m) where n = number of nodes and m = number of edges.

Space: We have to store the entire tree in order to traverse it. In addition, we are building up a array that is equal to the number of leaf nodes beneath our starting node. There our space complexity is O(k + f) where k = tree size and f = number of child nodes beneath the starting node.