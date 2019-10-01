# Complexity
* Time:O(nlogn)
* Space: O(tn + d = n) - where tn are the total number of nodes in the huffman tree, and d = the size of the encoded data string

# Explanation
This was a pretty daunting exercise at first, but once I got started, it proved to be a lot of fun! The time complexity here proved to be O(nlogn) because of the various sorts we perform in the construct_huffman_table method. 

The space complexity is essentially the size of the encoded data combined with the size of the created Huffman tree.

I tried to use recursion as much as possible for this exercise, with the expcetion of the while loop in the construct_tree method. One of the issues that I encountered using recursion was in the huffman_decoding method. In the earlier version of this method, I was trimming the bit_string to remove the bits I had already considered, however this proved to be the wrong approach as I had forgotten that strings are immutable. This meant that as soon as we broke out of our initial recursive method call, the string would revert to its original state annd would result in an infinite loop. The solution to this was to split the string out into an array that we then pass down into the recursive function. That allowed the function to mutate the array on all levels and progressively work our way through the bit_string/bit_array until it was empty.