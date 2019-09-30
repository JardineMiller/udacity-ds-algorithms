import sys
import queue
import heapq

class TreeNode:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

def get_frequencies_dict(string):
    frequencies = {}

    for char in string:
        entry = frequencies.get(char, None)

        if entry:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies

def construct_huffman_table(node, left=True, binary_string=""):
    if type(node) is str:
        return {node: binary_string}

    result = {}
    result.update(construct_huffman_table(node.left, True, binary_string + "0"))
    result.update(construct_huffman_table(node.right, False, binary_string + "1"))
    return result

def construct_tree(freq_dict):
    tuples_list = sorted(freq_dict.items(), key = lambda tup:tup[1]) 

    while len(tuples_list) > 1:
        # Take first two tuples
        char1, count1 = tuples_list[0]
        char2, count2 = tuples_list[1]

        # Remove from the list
        tuples_list = tuples_list[2:]

        # Create a parent node with each tuple chars as children
        parent_node = TreeNode(char1, char2)

        # Attach the node back into the list, the new count being the combined count of the children
        tuples_list.append((parent_node, count1 + count2))

        # Re-sort the list so we retain priority
        tuples_list = sorted(tuples_list, key = lambda tup:tup[1])

    return tuples_list[0][0]

def huffman_encoding(data):
    frequencies = get_frequencies_dict(data)
    tree = construct_tree(frequencies)
    huffman_table = construct_huffman_table(tree)
    encoded_data = ""

    for char in data:
        encoded_data += huffman_table[char]

    return (encoded_data, tree)

def huffman_decoding(data, tree, i=0):
    result = ""
    node = None

    while len(data) > 0:
        char = data[i]
        
        if node is None:
            node = tree

        if char == "0":
            node = node.left
        else:
            node = node.right

        i += 1
        
        if type(node) is str:
            data = data[i:]
            i = 0
            result += node
            node = None

    return result

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



# from collections import defaultdict