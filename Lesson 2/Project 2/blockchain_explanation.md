# Complexity
### n = number of blocks in blockchain

* Time: Traversal - O(n)
* Time: Insertion - O(1)
* Space: O(n)

# Explanation
Blockchains are functionally very similar to Linked Lists, so LL seemed like a sensible choice when decided upon the functionality of this blockchain. Linked Lists are fantastic for constant time insert/delete use operations, however to search for a particular value within the chain you are looking at a linear time complexity O(n) as you will have to visit each node (worst case) in order to find what you're looking for.

Another downside to blockchains is that you need to store the entire structure in order to have full visibility of it. The very nature of blockchains dictate that each person using/mining it needs a local version of the entire blockchain in order to validate it. Blockchains has been in popular use for the best part of a decade now so these blockchains are getting increasingly large. At the time of writing, the Bitcoin blockchain is 242GB. Whilst large, this chart: https://www.blockchain.com/en/charts/blocks-size helps to indicate that the increase of the blockchain's size - despite exponential use since its inception - increases on a linear scale.
