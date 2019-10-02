## Design:
This was a pretty daunting exercise at first, but once I got started, it proved to be a lot of fun!

I tried to use recursion as much as possible for this exercise, with the expcetion of the while loop in the construct_tree method. One of the issues that I encountered using recursion was in the huffman_decoding method. In the earlier version of this method, I was trimming the bit_string to remove the bits I had already considered, however this proved to be the wrong approach as I had forgotten that strings are immutable. This meant that as soon as we broke out of our initial recursive method call, the string would revert to its original state annd would result in an infinite loop. The solution to this was to split the string out into an array that we then pass down into the recursive function. That allowed the function to mutate the array on all levels and progressively work our way through the bit_string/bit_array until it was empty.

## Time Complexity
* Encoding:
There are four main components to the encoding aspect of this solution:

** get_frequencies_dict(): O(n)
** construct_tree(): O(nlogn)
** construct_huffman_table(): O(n)
** encode_string: O(n)

** Result: O(3n + nlogn) - simplified to O(nlogn)

To create our dictionary of characters to their frequency, we have to iterate over the entire string, meaning that is O(n) in time complexity. Next, we construct our huffman tree, which takes O(nlogn) time as we have to sort our list after each iteration to ensure that we are always dealing with the least-frequent nodes/characters. An alternative data structure to use here could have been a Priority Queue or Heap, but I decided to stick with a simpler implementation. After that, we have to iterate through the entire tree, visiting each node to construct the Huffman code for each character present in our string. Finally, we iterate over the original string one more time, finding the huffman code for each character (with O(1) lookup from the dict) and injecting it into our resulting encoded_data string.

* Decoding:
The decoding aspect takes two main steps:

** bit_string to bit_array: O(n)
** decode_char(): O(nm) where n (length of bit_arr) * m (number of levels in tree)

** Result: O(nm)

Here, we use the recursive function decode_char() to find the corresponding character for each Huffman code we find in our bit_string. This function must travel from the root to a leaf node each time it is called, therefore the wost case runtime is it has to traverse each level of the tree. If we call this function within a loop that iterates over the bit_array, then our run time for this will be O(nm) because it is highly unlikely that n and m will be of the same size.


## Space Complexity
* Encoding:
** get_frequencies_dict(): O(n) n = str length
** construct_tree(): O(n) n = number of distinct chars in str
** construct_huffman_table(): O(nm) n = number of leaf nodes in tree * m = number of levels in tree
** encode_string: O(n)

** Result: O(3n + nm) - simplified to O(nm)

* Decoding:
** bit_string to bit_array: O(n)
** decode_char(): O(nm) where n (length of bit_arr) * m (number of levels in tree)

** Result: O(nm)